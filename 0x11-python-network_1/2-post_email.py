#!/usr/bin/python3
"""Retrieves the value of the X-Request-Id header from a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)  # Exit with error code

    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            request_id = headers.get("X-Request-Id")

            if request_id:
                print(request_id)
            else:
                print("X-Request-Id header not found.")

    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
