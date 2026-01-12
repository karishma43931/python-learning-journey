"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: Number Analysis

Description:
This program analyzes a number to determine whether it is
positive, negative, or zero and also checks whether the
number is even or odd using nested conditions.
"""
n = int(input("Enter a number : "))

if n==0:
    print("Zero ")
else:
    if n>0:
        print("positive number")
    else:
        print("negative number")
    if n %2 ==0:
        print("Even Number")
    else:
        print("Odd Number")
