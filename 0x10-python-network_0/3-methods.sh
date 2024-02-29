#!/bin/bash
# use curl to get OPTIONS
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
