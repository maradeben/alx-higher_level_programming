#!/usr/bin/python3
""" script to add all arguments to Python list and save to file """
import sys
import json
import os
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"
fil = Path(filename)
fil.touch(exist_ok=True)
if os.stat(filename).st_size == 0:
    save_to_json_file([], filename)
else:
    data = load_from_json_file(filename)
    data.extend(args)
    save_to_json_file(data, filename)
