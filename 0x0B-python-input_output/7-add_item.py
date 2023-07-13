#!/usr/bin/python3
"""
module for adding all arguments to a python list and saves them to a file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    my_list = sys.argv[1:].copy()
    # check if file exist otherwise create it
    if not os.path.exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    if len(my_list) > 0:
        # load previous content and append
        my_list = load_from_json_file("add_item.json") + my_list
        # save new data
        save_to_json_file(my_list, "add_item.json")
