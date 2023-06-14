# 1.Write a Python program to check the validity of a password given by the user.
# The Password should satisfy the following criteria:
#     • Contain at least 1 letter between a and z
#     • Contain at least 1 number between 0 and 9
#     • Contain at least 1 letter between A and Z
#     • Contain at least 1 character from $, #, @
#     • Minimum length of password: 6
#     • Maximum length of password: 12

import re
password = input("Enter The Valid password\n")
check = True

while(True):
    if (len(password)>=12 & len(password)<=6):
        check = False
        break 

    if not re.search("[a-z]+", password):
        check = False
        break 

    if not re.search("[0-9]+", password):
        check = False
        break 

    if not re.search("[A-Z]+", password):
        check = False
        break 

    if not re.search("r'#|@|$'", password):
        check = False
        break 

    else:
        print("You are Enterd Valid Password\n" , password)
        break

if (check == False ):
    print("Please Input Valid Password")