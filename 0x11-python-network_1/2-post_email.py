#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import sys
from urllib import parse, request


if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
