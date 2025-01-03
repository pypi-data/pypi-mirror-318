# encoding: utf-8

'''JPL LabCAS Downloader: download implementation.'''

from functools import partial
from multiprocessing import Pool
from pathlib import Path
import logging, requests, urllib.parse, os, sys


_logger   = logging.getLogger(__name__)

_timeout  = 10        # How long to wait for the query to return (in seconds)
_max_rows = 99999999  # How many rows max to retrieve; this code breaks if there's more data than this
_bufsiz   = 512       # Buffer size in bytes for retrieving data


def _enumerate_files(url: str, data_id: str, auth: tuple) -> list:
    '''Enumerate files.

    This asks the data access API at ``url`` for the files that match the ``data_id``, using the optional
    ``auth`` tuple. It returns a list of matching URLs to fetch.
    '''
    _logger.debug('𝑓 _enumerate_files %s, %s, auth=%r', url, data_id, auth is not None)
    request_type = 'datasets' if '/' in data_id else 'collections'
    if not url.endswith('/'): url += '/'
    url = url + request_type + f'/list?rows={_max_rows}&q=id:' + data_id
    _logger.debug('Constructed URL for file list is «%s»', url)
    _logger.info('Requesting matching files for %s from the API', data_id)
    response = requests.get(url, timeout=_timeout, auth=auth)
    matches = [i for i in response.text.split('\n') if i.strip()]
    _logger.info('Got %d files', len(matches))
    return matches


def _fetch(url: str, target: Path, auth: tuple):
    '''Fetch data.

    This retrieves the file at ``url`` and writes it to ``target``, using ``auth`` to log in if
    it's not None.
    '''
    _logger.debug('𝑓 _fetch %s to %s, auth=%r', url, target, auth is not None)

    # Can we use _logger with multiprocessing?
    print(f'𝑓 _fetch {url} to {target}', file=sys.stderr)

    rel_path = urllib.parse.unquote(url.split('id')[1][1:])
    response = requests.get(url, stream=True, auth=auth)
    os.makedirs(os.path.join(target, os.path.dirname(rel_path)), exist_ok=True)
    with open(os.path.join(target, rel_path), 'wb') as outfile:
        for chunk in response.iter_content(chunk_size=_bufsiz):
            if chunk: outfile.write(chunk)


def download(url: str, data_id: str, target: Path, username: str, password: str, concurrency: int):
    '''Download data from LabCAS.

    This accesses the LabCAS API at ``url``, authenticating with ``username`` and ``password`` to
    retrieve the collection or dataset identified by ``data_id`` and writing the data to ``target``.
    Multiple files will be downloaded at the same time based on ``concurrency``.
    '''
    if username and password:
        auth = (username, password)
    else:
        auth = None

    files = _enumerate_files(url, data_id, auth)
    with Pool(processes=concurrency) as pool:
        fetcher = partial(_fetch, target=target, auth=auth)
        pool.map(fetcher, files)


if __name__ == '__main__':
    # For multiprocessing to work, we need this ifmain block; it doesn't actually need
    # to do anything, though.
    #
    # Also, logging doesn't work in forked processes.
    print('IN jpl.labcas.downloader._download ifmain', file=sys.stderr)
