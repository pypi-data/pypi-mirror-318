# encoding: utf-8

'''JPL LabCAS Downloader: main entrypoint'''

from . import VERSION
from ._download import download_by_id, download_by_query
from pathlib import Path
import argparse, logging, getpass, os, sys

_defaultURL  = 'https://edrn-labcas.jpl.nasa.gov/data-access-api/'
_defaultDir  = '.'


def main():
    parser = argparse.ArgumentParser(description='Download data from a LabCAS server')
    parser.add_argument('--version', action='version', version=VERSION)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-d', '--debug',
        action='store_const', const=logging.DEBUG, default=logging.INFO, dest='loglevel',
        help='Log copious debugging messages suitable for developers'
    )
    group.add_argument(
        '-q', '--quiet',
        action='store_const', const=logging.WARNING, dest='loglevel',
        help="Don't log anything except warnings and critically-important messages"
    )
    parser.add_argument(
        '-u', '--username', default=os.getenv('LABCAS_USERNAME'),
        help='User ID with which to authenticate, defaults to LABCAS_USERNAME if set; if unset, uses no authentication'
    )
    parser.add_argument(
        '-p', '--password', default=os.getenv('LABCAS_PASSWORD'),
        help='Password with which to authenticate, defaults to LABCAS_PASSWORD, or prompts if neither is given'
    )
    parser.add_argument(
        '-a', '--api', default=os.getenv('LABCAS_API_URL', _defaultURL),
        help='API endpoint to access, defaults to LABCAS_API_URL [%(default)s]'
    )
    parser.add_argument(
        '-c', '--concurrency', default=10, help='№ of simultaneous downloads to support ([%(default)s])'
    )
    parser.add_argument(
        '-f', '--file-query', action='store_true',
        help='Use a file query instead of a collection/dataset identifier'
    )
    parser.add_argument('-t', '--target', default=_defaultDir, help='Target directory [%(default)s]')
    parser.add_argument('data', metavar='DATA-ID', help='Collection or collection/dataset to retrieve; or a file query')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel, format="%(levelname)s %(message)s")

    concurrency = int(args.concurrency)
    if concurrency < 1:
        raise ValueError(f'Concurrency {concurrency} is too low; try at least 1')

    if args.username:
        password = args.password if args.password else getpass.getpass(f"{args.username}'s password: ")
    else:
        password = None

    target = Path(os.path.abspath(args.target))
    os.makedirs(target, exist_ok=True)

    if args.file_query:
        download_by_query(args.api, args.data, target, args.username, password, concurrency)
    else:
        download_by_id(args.api, args.data, target, args.username, password, concurrency)
    sys.exit(0)


if __name__ == '__main__':
    main()
