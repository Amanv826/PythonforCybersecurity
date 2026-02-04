#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Aman Vohra on 2/4/2026

#prompt for the source message
source_message = input("what is the message to encrypt/decrypt")
#convert message to lower case for simplicity
source_message = source_message.lower()
final_message = ""
#Loop through each letterf in the source message
for letter in source_message:
    #convert the letter to the ASCII equivelent
    ascii_num = ord(letter)
    #check to see if an alphabetic (a-z) character, if not, skip
    if ascii_num >= 97 and ascii_num <=122:
            #Add 13 to ascii_num to "shift" it by 13
        new_ascii = ascii_num + 13
        #confirm new character will be alphabetic
        if  new_ascii > 122:
            #if not, wrap around
            new_ascii = new_ascii - 26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)
#print converted message
print("Message has been converted:")
print(final_message)

