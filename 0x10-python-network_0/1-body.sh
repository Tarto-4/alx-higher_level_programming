#!/bin/bash
# Display the body of the response from the URL passed as argument if the request was successful
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
