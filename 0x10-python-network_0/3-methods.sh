#!/bin/bash
# display all HTTP methods acceptable to server
curl -sI "$1" | grep "Allow" | cut -d" " -f2-
