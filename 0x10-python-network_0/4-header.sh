#!/bin/bash
# Display the body of the response from the URL passed as argument after sending a GET request with custom header
curl -s -H "X-School-User-Id: 98" "$1"
