"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Basic Login Authentication

Description:
This program validates user login credentials by comparing
the entered username and password with predefined values.
"""
Username = input("Enter your username : ")
Password = input("Enter your password : ")
correct_username = "admin"
correct_password = "admin123"
if Username == correct_username and Password == correct_password:
    print("Login Successful")
else:
    print("Invalid Login")

# Difficulty: Medium
# Program: Detailed Login Validation
Username1 = input("Enter your username : ")
Password2 = input("Enter your password : ")
correct_username1 = "admin"
correct_password1 = "admin123"
if Username1 == correct_username1 and Password2 == correct_password1:
    print("Login Successful")
elif Username1 != correct_username1 and Password2 == correct_password1:
    print("Enter Correct Username")
elif Username1 == correct_username1 and Password2 != correct_password1:
    print("Enter Correct Password")
else:
    print("Invalid Credentials")