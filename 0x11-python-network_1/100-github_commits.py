#!/usr/bin/python3
"""
Reads 10 github commits from user rails using the GitHub API
"""
import requests


if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/rails/rails/commits")
    for commit in res.json()[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
