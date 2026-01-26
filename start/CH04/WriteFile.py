#!/usr/bin/env python3
# Sample script that writes to a file
# By Aman Vohra on 1/26/26

#open file for  wirting
hackerinfo = open("hackme.txt", "w")

#questions to collect info
print("Answer the following questions")

name = input("What is your name? ")
favorite_color = input ("What is your favorite color? ")
first_pet_name = input ("what is your first pet's name? ")
mothers_maiden_name = input ("What is your mohter's maiden name? ")
elementary_school = input ("What elementary school did you go to? ")

#write to the file
hackerinfo.write("Name:" + name + "\n")
hackerinfo.write("Favorite color: " + favorite_color + "\n")
hackerinfo.write("First pet's name: " + first_pet_name + "\n")
hackerinfo.write("Mother's maiden name: " + mothers_maiden_name + "\n")
hackerinfo.write("Elementary school: " + elementary_school + "\n")


