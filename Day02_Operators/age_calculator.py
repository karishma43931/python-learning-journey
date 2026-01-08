"""
Day 2 – Python Basics
Difficulty: Easy
Program: Age Calculator
Description:
This program calculates the user's age based on the current year
and birth year using type casting and arithmetic operations.
"""
name = input("Enter your name: ")
birth_year = int(input("Enter Birth Year: "))
current_year = int(input("Enter Current Year: "))
user_age = current_year - birth_year
print(f"Hi! {name}.\nYour Age based on current year:{current_year} and birth year:{birth_year} is : {user_age}")
