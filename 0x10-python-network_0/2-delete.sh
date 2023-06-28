#!/bin/bash
# send DELETE request to first arg and display response body
curl -X DELETE -s "$1"
