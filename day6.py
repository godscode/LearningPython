#write a Program to check the validity of password input by user.

'''
Password validity rules:
A Valid Pasword must have:

Be at leat 8 characters long.
Contain at least one uppercase letter.
Contain at least one lowercase letter.
Contain at least one digit (0-9).
Contain at least one special character (e.g., @, #, $, %, &, *, etc.).
Contain no spaces.

'''

import string
special_characters = string.punctuation

#Be at leat 8 characters long.
def valid_entered_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")

#define the flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    #special_characters = "!@#$%^&*()-+?_=,<>/"

#check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

#validate all conditions
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:   
        return "Password must contain at least one lowercase letter."       
    if not has_digit:
        return "Password must contain at least one digit (0-9)."
    if not has_special:
        return "Password must contain at least one special character (e.g., @, #, $, %, &, *, etc.)."
    if not password:
        return "Password can not be empty."
    else:
       return "Password is valid."

try:
    password = input("Enter your password: ")
    if not password:
        raise ValueError("Password cannot be empty.")
    result = valid_entered_password(password)
    print(result)
except ValueError as e:
    print(e)

#fire the function to check the password
valid_entered_password(password)


