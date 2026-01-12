"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Largest of Two Numbers

Description:
This program compares two numbers entered by the user and
prints which number is greater or if both numbers are equal.
"""
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is less than {b}")
elif a==b:
    print(f"Both {a} and {b} are Equal")
