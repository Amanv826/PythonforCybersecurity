#!/usr/bin/env python3
test_file = open("testfile.txt","w")

#write line to a file
print("hello world")
print("have a good day")
test_file.write("Hello There\n")
test_file.write("Nice to see you\n")
test_file.write("Come back again\n")


#Close the file
test_file.close()
                