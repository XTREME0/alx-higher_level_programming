#!/bin/bash
# use curl to get only status
curl -sI -o /dev/NULL -w "%{http_code}" "$1"
