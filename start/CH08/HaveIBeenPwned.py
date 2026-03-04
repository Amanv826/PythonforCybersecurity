#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Aman Vohra 3/4/2026

#import modules
import hashlib
import requests

#funciton to check the password
def check_pwned (sha_prefix):
    pwned_dictionary = {}

    #Perform API request
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get (request_uri)

    #Confirm if hash was found
    pwned_list = results.text.split("\r\n")
    for pwned_password in pwned_list:
        temp_password = pwned_password.split(":")
        pwned_dictionary[temp_password[0]] = temp_password [1]
    return pwned_dictionary


#prompt to enter password
new_password = input ("What password would you like me to check?")

#Hash the password
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()

#Split the password
sha_prefix = hashed_password [0:5]
sha_suffix = hashed_password [5:].upper()

#Check the password
check_pwned (sha_prefix)
pwned_dictionary = check_pwned (sha_prefix)
#check the result of password
if sha_suffix in pwned_dictionary:
    print ("Password has been compromised {0} times".format (pwned_dictionary [sha_suffix]))
else:
    print ("Password has not been found, it's safe to use!")