#!/usr/bin/python3
""" Send mail thru link """
if __name__ == "__main__":
    import urllib.request
    import sys
    r = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(r) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.URLError as err:
        print(f'Error code: {err.code}')
