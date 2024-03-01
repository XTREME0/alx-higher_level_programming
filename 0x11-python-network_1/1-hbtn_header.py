#!/usr/bin/python3
""" get the value of var """
if __name__ == "__main__":
    import urllib.request
    import sys
    if len(sys.argv) == 1:
        exit(-1)
    with urllib.request.urlopen(sys.argv[1]) as resp:
        hd = resp.info()
        print(hd['X-Request-Id'])
