#!/bin/bash
# use curl to get OPTIONS
curl -sXI OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
