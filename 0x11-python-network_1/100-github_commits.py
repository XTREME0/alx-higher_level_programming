#!/usr/bin/python3
""" use github api """

if __name__ == "__main__":
    import sys
    import requests
    r = requests.get(f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits')
    c = 10
    for commit in r.json():
        print(f'{commit.get("sha")}: {commit.get("author").get("login")}')
        c -= 1
        if not c:
            break
