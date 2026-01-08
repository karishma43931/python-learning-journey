"""
Day 2 – Python Basics
Difficulty: Medium
Program: Life Remaining Weeks Calculator
Description:
This program calculates the number of weeks remaining assuming
a lifespan of 90 years .
"""

life_span = int(90)
name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
remaining_years = life_span - user_age
one_year_to_week = int(365/7)
remaining_years_to_weeks = one_year_to_week * remaining_years
print(f"Hey {name}!\nAssuming the lifespan of  Human is 90 years.\nwe calculated the number of weeks You have to see this beautiful world is: {remaining_years_to_weeks}Weeks!")