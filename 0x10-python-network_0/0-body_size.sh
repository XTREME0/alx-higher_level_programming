#!/bin/bash
# get the content length
curl -s "$1" -i | awk '/Content-Length/ { print $2 }'
