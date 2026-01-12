"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Even or Odd Number

Description:
This program takes an integer input from the user and checks
whether the given number is even or odd using the modulus (%)
operator and if-else conditional statements.
"""
n = int(input("Enter a number: "))
if n==0:
    print(f"{n} is Nor Even nor odd Number")
elif n%2 ==0:
    print(f"{n} is Even Number")
elif n%2 !=0:
    print(f"{n} is Odd Number")
