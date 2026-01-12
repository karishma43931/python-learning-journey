"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: Student Grading System

Description:
This program assigns grades to a student based on their marks
using predefined grading criteria and conditional statements.
"""
n1 = int(input("Enter Marks 1-100 : "))
if n1>=90:
    print(f"YAY you Got A Grade")
elif 75<=n1<=89:
    print(f"YOU Got B Grade")
elif 50<=n1<=74:
    print(f"YOU Got C Grade")
else:
    print("Fail")