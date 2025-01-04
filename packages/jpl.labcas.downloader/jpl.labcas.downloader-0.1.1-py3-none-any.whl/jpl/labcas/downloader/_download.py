# encoding: utf-8

'''JPL LabCAS Downloader: download implementation.'''

from functools import partial
from http import HTTPStatus
from multiprocessing import Pool, Process, Queue, JoinableQueue
from pathlib import Path
from typing import Generator
import logging, requests, urllib.parse, os, sys


_logger   = logging.getLogger(__name__)

_timeout   = 10        # How long to wait for the query to return (in seconds)
_max_rows  = 99999999  # How many rows max to retrieve; this code breaks if there's more data than this
_bufsiz    = 512       # Buffer size in bytes for retrieving data
_file_rows = 100       # For file query, how many rows to get at a time


def _enumerate_files(url: str, data_id: str, auth: tuple) -> list:
    '''Enumerate files.

    This asks the data access API at ``url`` for the files that match the ``data_id``, using the optional
    ``auth`` tuple. It returns a list of matching URLs to fetch.
    '''
    _logger.debug('𝑓 _enumerate_files %s, %s, auth=%r', url, data_id, auth is not None)
    request_type = 'datasets' if '/' in data_id else 'collections'
    if not url.endswith('/'): url += '/'
    url = url + request_type + f'/list?rows={_max_rows}&q=id:' + data_id + '*'
    _logger.debug('Constructed URL for file list is «%s»', url)
    _logger.info('Requesting matching files for %s from the API', data_id)
    response = requests.get(url, timeout=_timeout, auth=auth)
    if response.status_code == HTTPStatus.OK:
        matches = [i for i in response.text.split('\n') if i.strip()]
        _logger.info('Got %d files', len(matches))
        return matches
    else:
        raise ValueError(f'Unexpected status {response.status_code} from {response.url}')


def _fetch(url: str, target: Path, auth: tuple):
    '''Fetch data.

    This retrieves the file at ``url`` and writes it to ``target``, using ``auth`` to log in if
    it's not None.
    '''
    _logger.debug('𝑓 _fetch %s to %s, auth=%r', url, target, auth is not None)

    # Can we use _logger with multiprocessing?
    print(f'𝑓 _fetch {url} to {target}', file=sys.stderr)

    rel_path = urllib.parse.unquote(urllib.parse.urlparse(url).query[3:])
    response = requests.get(url, stream=True, auth=auth)
    os.makedirs(os.path.join(target, os.path.dirname(rel_path)), exist_ok=True)
    with open(os.path.join(target, rel_path), 'wb') as outfile:
        for chunk in response.iter_content(chunk_size=_bufsiz):
            if chunk: outfile.write(chunk)


def download_by_id(url: str, data_id: str, target: Path, username: str, password: str, concurrency: int):
    '''Download a collection or dataset ID's worth of data from LabCAS.

    This accesses the LabCAS API at ``url``, authenticating with ``username`` and ``password`` to
    retrieve the collection or dataset identified by ``data_id`` and writing the data to ``target``.
    Multiple files will be downloaded at the same time based on ``concurrency``.

    If ``data_id`` contains a `/`, it's considered a COLLECTION/DATASET, and the LabCAS backend's
    dataset list API is used to enumerate the files to download. Otherwise, it's a COLLECTION and
    the collection list API is used instead.
    '''
    if username and password:
        auth = (username, password)
    else:
        auth = None

    files = _enumerate_files(url, data_id, auth)
    with Pool(processes=concurrency) as pool:
        fetcher = partial(_fetch, target=target, auth=auth)
        pool.map(fetcher, files)


def _enumerate_files_by_query(url, query, auth) -> Generator[str, None, None]:
    '''Enumerate files with the given Solr ``query`` on the files lister API.'''
    if not url.endswith('/'): url += '/'
    url, start = f'{url}/files/list', 0
    while True:
        params = {'q': query, 'start': start, 'rows': _file_rows}
        response = requests.get(url, timeout=_timeout, auth=auth, params=params)
        if response.status_code == HTTPStatus.OK:
            matches = [i for i in response.text.split('\n') if i.strip()]
            num = len(matches)
            if num == 0: return
            start += num
            for match in matches: yield match
        else:
            raise ValueError(f'Unexpected status {response.status_code} from {response.url}')


def _file_url_producer(queue: Queue, concurrency: int, url: str, query: str, auth: tuple):
    '''Producer that puts URLs to download into the given ``queue``.'''
    for url in _enumerate_files_by_query(url, query, auth): queue.put(url)

    # Signal to consumers that no more items are added
    for _ in range(concurrency): queue.put(None)


def _file_download_consumer(queue: Queue, target: Path, auth: tuple):
    '''Consumer that downloads URLs named in the ``queue`` to the ``target``.'''
    while True:
        url = queue.get()
        if url is None:
            queue.task_done()
            break
        try:
            rel_path = urllib.parse.unquote(urllib.parse.urlparse(url).query[3:])
            response = requests.get(url, stream=True, auth=auth)
            os.makedirs(os.path.join(target, os.path.dirname(rel_path)), exist_ok=True)
            with open(os.path.join(target, rel_path), 'wb') as outfile:
                print(f'𝕗 Downloading {target} to {rel_path}', file=sys.stderr)
                for chunk in response.iter_content(chunk_size=_bufsiz):
                    if chunk: outfile.write(chunk)
        except requests.RequestException:
            _logger.exception('Failed to download %s', url)
        finally:
            queue.task_done()


def download_by_query(url: str, query: str, target: Path, username: str, password: str, concurrency: int):
    '''Download data from LabCAS based on a file query.

    This accesses the LabCAS API at ``url``, authenticating with ``username`` and ``password`` to
    retrieve files matching the given ``query`` and writing the data to ``target``. Multiple files
    will be downloaded at the same time based on ``concurrency``.
    '''
    if username and password:
        auth = (username, password)
    else:
        auth = None

    queue = JoinableQueue()
    producer_process = Process(target=_file_url_producer, args=(queue, concurrency, url, query, auth))
    producer_process.start()
    consumers = [
        Process(target=_file_download_consumer, args=(queue, target, auth))
        for _ in range(concurrency)
    ]
    for c in consumers: c.start()
    producer_process.join()
    queue.join()
    for c in consumers: c.join()


if __name__ == '__main__':
    # For multiprocessing to work, we need this ifmain block; it doesn't actually need
    # to do anything, though.
    #
    # Also, logging doesn't work in forked processes.
    print('IN jpl.labcas.downloader._download ifmain', file=sys.stderr)
