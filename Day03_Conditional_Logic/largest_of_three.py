"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: Largest of Three Numbers

Description:
This program takes three numbers as input and determines
the largest among them using conditional logic.
"""
a = int(input("Enter a number1 : "))
b = int(input("Enter a number2 : "))
c = int(input("Enter a number3 : "))
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"{c} is greater than {a} and {b}")