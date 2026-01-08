"""
Day 2 – Python Basics
Difficulty: Medium
Program: Age and Salary Summary
Description:
This program takes age and monthly salary as input and calculates
annual salary and years left until retirement.
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
retirement_age = int(input("Enter your retirement age as per company policies: "))
monthly_salary = int(input("Enter your monthly salary: "))
Annual_salary = monthly_salary * 12
remaining_service = (retirement_age - age)
print(f"Hey {name}!,\nYour Annual Salary is RS.{Annual_salary} and\nYou have {remaining_service}Years for your retirement .")
