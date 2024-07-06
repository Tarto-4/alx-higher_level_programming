#!/usr/bin/python3
"""Retrieves the value of the X-Request-Id header from a given URL.

Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            headers = dict(response.headers)  # Convert headers to dictionary
            request_id = headers.get('X-Request-Id') 

            if request_id:
                print(request_id)
            else:
                print("X-Request-Id header not found.")

    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
