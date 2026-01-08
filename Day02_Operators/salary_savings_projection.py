"""
Day 2 – Python Basics
Difficulty: Hard
Program: Salary Savings Projection
Description:
This program calculates yearly savings based on monthly salary,
monthly expenses, and savings percentage using type casting.
"""
name = input("Enter your name: ")
monthly_salary = int(input("Enter your monthly salary: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_salary - monthly_expenses
yearly_salary = monthly_salary *12
yearly_savings = monthly_savings*12
savings_percentage = float((yearly_savings/yearly_salary)*100)
print(f"Monthly savings: {monthly_savings}")
print(f"Yearly savings: {yearly_savings}")
print(f"Yearly Savings in percentage:{savings_percentage:.2f}")