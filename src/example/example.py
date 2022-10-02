import argparse

import requests

def resolve_args():
    parser = argparse.ArgumentParser(
        prog='Example App',
        description='Example application to be created with `build`.'
    )
    parser.add_argument(
        '--url', '-u',
        action='store',
        dest='url'
    )
    return parser.parse_args()

def get(url: str, verify: bool = True) -> requests.Response | bool:
    try:
        r = requests.get(url=url, verify=verify)
        r.raise_for_status()
        print(f'Status: {r.status_code}, Reason: {r.reason}')
        return r
    except requests.exceptions.RequestException as e:
        print(e)
        print(f'Status: {r.status_code}, Reason: {r.reason}')
        return False

def get_entrypoint():
    args = resolve_args()
    get(url=args.url)
    return 0
