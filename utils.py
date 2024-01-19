import requests
import sys
from requests.exceptions import HTTPError


def make_http_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except Exception as err:
        print(f"Other error occurred: {err}")
        sys.exit(1)
