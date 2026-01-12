"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Positive, Negative or Zero Check

Description:
This program accepts a number from the user and determines
whether the number is positive, negative, or zero using
conditional statements.
"""
n1 = int(input("Enter a number: "))
if n1 ==0:
    print(f"{n1} is Zero")
elif n1>0:
    print(f"{n1} is Positive Number")
elif n1<0:
    print(f"{n1} is Negative Number")
