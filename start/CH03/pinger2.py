#!/usr/bin/env python3
# Second example of pinging from Python
# By 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

test_file = open(dir_path + "/testfile.txt", "r")
#Read file and print to screen
contents = test_file.read()
print (contents)

#close the file
test_file.close()
