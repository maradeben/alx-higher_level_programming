#!/bin/bash
# post JSON from a file
curl -X POST \
	-H "Content-Type: application/json" \
	-d @$2 \
	$1
