#!/usr/bin/python3
""" fetch a website """
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        content = resp.read()
        print("Body response:")
        print(f'\t- type: {type(content)}\n\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
