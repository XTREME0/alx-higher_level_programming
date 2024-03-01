#!/usr/bin/python3
""" Send mail thru link """
if __name__ == "__main__":
    import urllib.request
    import sys
    if len(sys.argv) > 3:
        exit(-1)
    d = urllib.parse.urlencode('email': sys.argv[2]).encode("utf-8")
    r = urllib.request.Request(sys.argv[1], d)
    with urllib.request.urlopen(r) as resp:
        print(resp.read().decode("utf-8"))
