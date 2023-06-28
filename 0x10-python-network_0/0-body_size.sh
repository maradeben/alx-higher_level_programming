#!/bin/bash
# get content length from curl response
curl -s "$1" | wc -c
