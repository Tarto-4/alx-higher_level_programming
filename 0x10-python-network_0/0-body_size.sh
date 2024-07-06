#!/bin/bash
# Display the size of the body of the response from the URL passed as argument
curl -sI "$1" | grep -i Content-Length | cut -d' ' -f2
