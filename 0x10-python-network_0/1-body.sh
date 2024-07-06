#!/bin/bash
# Display the body of the response from the URL passed as argument if status is 200
curl -s "$1" | grep "HTTP/1.1 200" > /dev/null && curl -s "$1"
