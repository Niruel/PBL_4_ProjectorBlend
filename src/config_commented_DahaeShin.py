#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:37:09 2020

@author: dahaeshin
"""

#config file
"""
@brief  Header main configure to read values from the ini file
"""

"""
import config parser to read and write ini file
"""
import configparser 

"""
act based on configparser contents
"""
config = configparser.ConfigParser()

"""
use the read() method of SafeConfigParser to read the configuration file
"""
config.read('config.ini') 

print("List all contents")

for section in config.sections():
    """
    get section from the ini file
    """
    item_list = config.items(section) 
    
    print("\nSection: " + section)
    
    for item in item_list:
        """
        get key from the ini file
        """
        key = item[0]   
        """
        get value from the ini file
        """
        value = item[1]
        print("key : " + key + ", value : " + value)
