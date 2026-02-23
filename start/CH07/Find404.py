#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Aman Vohra 2/18/26

import os

#prompt for file and open
log_file = input("Which file do not want to scan?")
dir_path = os.path.dirname(os.path.realpath(__file__))
f= open(dir_path + "/" + log_file, "r")

#Read file line by line
while True: 
    line = f.readline()
    if not line:
        break
    #look for 404 and print
    if "404" in line: 
        print(line.strip())
#close file
f.close()