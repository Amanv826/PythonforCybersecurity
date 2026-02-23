#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Aman Vohra on 2/9/2026

#import moudules
import os
import crypt
#function to test password
def test_password(algo_salt, hashed_password, password_guess):
    #Use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algo_salt)
    #Compare salted guess against hashed password
    if hashed_guess == hashed_password: 
        return True
    return False
#load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path + "/top10000000.txt", "r")
passwords = f .readlines()
#Prompt user for Algorithm/Salt
algorithm_salt = input("What is the algorith and salt?")
#Prompt user for salted hash
hashed_pasword = input ("What is the full hased password?")
#Loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_pasword, password)
    if result:
        print("Match found: {0}".format (password))
        break