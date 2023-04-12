#!/usr/bin/python3
""" script to add all arguments to Python list and save to file """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"
data = []
if os.path.exists(filename):
    data = load_from_json_file(filename)
data.extend(args)
save_to_json_file(data, filename)
