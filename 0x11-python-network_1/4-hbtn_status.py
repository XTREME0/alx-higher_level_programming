#!/usr/bin/python3
""" fetch a website """
if __name__ == "__main__":
    import requests
    r = requests.get("https://alx-intranet.hbtn.io/status")
        print("Body response:")
        print(f'\t- type: {type(r.text)}\n\t- content: {r.text}')
