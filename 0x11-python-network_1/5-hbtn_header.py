#!/usr/bin/python3
"""
Takes in a URL, send a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
