"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Pass or Fail Check

Description:
This program checks whether a student has passed or failed
based on their marks. Passing marks are 35 or above.
"""
n = int(input("Enter Your Marks in the Range of 1-100 : "))
if n>=35:
    print(f"Congragulations you Passed the Test")
else:
    print(f"oh..no.. We are Sorry,"
          f"\nTo Pass the Test - He/She should aquire 35 Marks or greater")
