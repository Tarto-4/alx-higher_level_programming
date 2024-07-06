#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status with improved error handling."""

import urllib.request
import urllib.error  # Import for explicit error handling

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
