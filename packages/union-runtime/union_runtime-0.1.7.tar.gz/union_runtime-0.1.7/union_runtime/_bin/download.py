"""Module for downloading files from object stores."""

import logging
import os
import tarfile
from concurrent.futures import ThreadPoolExecutor
from tempfile import TemporaryDirectory
from threading import Lock
from time import sleep
from typing import List, Tuple
from urllib.parse import urlparse

import obstore

FILES_TAR_FILE_NAME = "include-files.tar.gz"
INTERNAL_APP_ENDPOINT_PATTERN = os.getenv("INTERNAL_APP_ENDPOINT_PATTERN")
DEFAULT_CHUNK_SIZE = 10 * 1024 * 1024

logger = logging.getLogger(__name__)


def _generate_url_query_name(app_name: str, pattern: str = INTERNAL_APP_ENDPOINT_PATTERN) -> str:
    return pattern.replace("{app_fqdn}", app_name)


def _extract_bucket_and_path(uri: str) -> Tuple[str, str]:
    parsed_uri = urlparse(uri)
    bucket_name = parsed_uri.netloc
    path_name = parsed_uri.path.lstrip("/")

    return bucket_name, path_name


# TODO: When obstore updates to 0.3.0, use start, end for obstore.get_range
def _download_chunk(store, path_name: str, offset: int, length: int):
    failed_reads = 0
    while True:
        try:
            return obstore.get_range(store, path_name, offset, length)
        except Exception:
            failed_reads += 1
            sleep(min(1.7**failed_reads * 0.1, 15))
            continue


def _download_chunk_and_write(store, f_obj, lock, path_name: str, offset: int, length: int):
    data = _download_chunk(store, path_name, offset, length)
    with lock:
        f_obj.seek(offset)
        f_obj.write(data)


def _download_file(store, path_name: str, dest: str, chunk_size: int = DEFAULT_CHUNK_SIZE):
    """Download a single file from path_name to dest."""
    meta = obstore.head(store, path_name)
    size = meta["size"]

    n_chunks = size // chunk_size
    lock = Lock()

    with open(dest, "wb") as f:
        with ThreadPoolExecutor() as executor:
            for n_chunk in range(n_chunks):
                executor.submit(
                    _download_chunk_and_write,
                    store,
                    f,
                    lock,
                    path_name,
                    n_chunk * chunk_size,
                    chunk_size,
                )

            # There is one more uneven chunk
            remainder = size % chunk_size
            if remainder > 0:
                executor.submit(
                    _download_chunk_and_write,
                    store,
                    f,
                    lock,
                    path_name,
                    n_chunks * chunk_size,
                    remainder,
                )


def get_store(uri: str, bucket: str):
    if uri.startswith("s3://") or uri.startswith("s3a://"):
        from obstore.store import S3Store

        return S3Store.from_env(bucket=bucket)
    elif uri.startswith("gs://"):
        from obstore.store import GCSStore

        return GCSStore.from_env(bucket=bucket)
    else:
        raise RuntimeError(f"protocol in {uri} does not work")


def download_code(uri: str, dest: str):
    logger.debug(f"Downloading code from {uri} to {dest}")
    bucket, path_name = _extract_bucket_and_path(uri)

    store = get_store(uri, bucket)

    # Simplify when Python 3.12+ only, by always setting the `extract_kwargs`
    # https://docs.python.org/3.12/library/tarfile.html#extraction-filters
    extract_kwargs = {}
    if hasattr(tarfile, "data_filter"):
        extract_kwargs["filter"] = "data"

    with TemporaryDirectory() as temp_dir:
        temp_dest = os.path.join(temp_dir, FILES_TAR_FILE_NAME)
        _download_file(store, path_name, temp_dest)

        with tarfile.open(temp_dest, "r:gz") as tar:
            tar.extractall(path=dest, **extract_kwargs)


def download_single_file(uri: str, dest: str) -> str:
    logger.info(f"Downloading file from {uri} to {dest}")
    bucket, path_name = _extract_bucket_and_path(uri)

    dest_path = os.path.join(dest, path_name)
    parent_dest = os.path.dirname(dest_path)
    if not os.path.exists(parent_dest):
        os.makedirs(parent_dest)

    # TODO: Support other object stores
    store = get_store(uri, bucket)

    _download_file(store, path_name, dest_path)
    return dest_path


def download_directory(uri: str, dest: str) -> str:
    logger.info(f"Downloading directory from {uri} to {dest}")
    bucket, path_name = _extract_bucket_and_path(uri)

    store = get_store(uri, bucket)
    all_records = obstore.list(store, prefix=path_name)
    for records in all_records:
        for record in records:
            src = record["path"]
            rel_dest_path = os.path.relpath(src, path_name)
            dest_path = os.path.join(dest, rel_dest_path)

            dirname = os.path.dirname(dest_path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            logger.info(f"Downloading file from {bucket}/{src} to {dest_path}")
            _download_file(store, src, dest_path)

    return dest


def download_inputs(user_inputs: List[dict], dest: str) -> Tuple[dict, dict]:
    logger.debug(f"Downloading inputs for {user_inputs}")

    output = {}
    env_vars = {}
    for user_input in user_inputs:
        # Support both download and auto_download to be backward compatible with
        # older union sdk versions
        if user_input.get("download", False) or user_input.get("auto_download", False):
            user_dest = user_input["dest"] or dest
            user_dest = os.path.abspath(user_dest)
            if user_input["type"] == "file":
                value = download_single_file(user_input["value"], user_dest)
            elif user_input["type"] == "directory":
                value = download_directory(user_input["value"], user_dest)
            else:
                raise ValueError("Can only download files or directories")
        else:
            # Resolve url query
            value = user_input["value"]
            if user_input["type"] == "url_query":
                value = _generate_url_query_name(value)

        output[user_input["name"]] = value

        if user_input["env_name"] is not None:
            env_vars[user_input["env_name"]] = value

    return output, env_vars
