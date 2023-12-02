#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(res.text)))
    print("    - content: {}".format(res.text))
