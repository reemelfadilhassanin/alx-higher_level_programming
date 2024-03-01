#!/usr/bin/python3
"""Holberton School staff evaluates candidates
    applying for a back-end position with multiple technical
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    re = requests.get(url)

    commits = re.json()[:10]

    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
