#!/bin/bash
# send post request to URL and display response body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
