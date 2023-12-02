#!/usr/bin/python3
"""
Take in a URL, send a request to the URL and display the body of the
response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
import sys
import requests


if __name__ == "__main__":
    try:
        with requests.get(sys.argv[1]) as response:
            print(response.text)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code >= 400:
            print("Error code: {}".format(e.response.status_code))
