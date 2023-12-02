#!/usr/bin/python3
"""
Reads 10 github commits from user rails using the GitHub API
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    ))
    for commit in res.json()[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
