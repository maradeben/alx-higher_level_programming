#!/bin/bash
# get content length from curl response

curl -I "$1" | grep "Content-Length: " | cut -d" " -f2
