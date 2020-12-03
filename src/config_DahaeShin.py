#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:37:09 2020

@author: dahaeshin
"""

#config file

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print("List all contents")

for section in config.sections():
    item_list = config.items(section)
    print("\nSection: " + section)
    for item in item_list:
        key = item[0]
        value = item[1]
        print("key : " + key + ", value : " + value)