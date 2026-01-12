"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: Leap Year Checker

Description:
This program checks whether a given year is a leap year based
on standard leap year rules using conditional statements.
"""
year = int(input("Enter Year : "))
if year%400 ==0 :
    print(f"{year} is a leap Year")
elif year%4 ==0 and year%100!=0:
    print(f"{year} is a leap Year")
else:
    print(f"{year} is not a leap Year")
