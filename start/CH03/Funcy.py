#!/usr/bin/env python3
# example workign with Functions
#By Aman Vohra 1/21/26

#prompt use to answer a question
good_day_question = "Is today a good day? (y/n) "
user_response = input(good_day_question)
#Store in variable

#if yes print a response
if user_response == "y":
    for count in range(10):
        print("Yes it is")
elif user_response == "Y":
    print("That's amazing")
else:
    print("I hope it gets better.")


