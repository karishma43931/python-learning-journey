"""
Day 2 – Python Basics
Difficulty: Medium
Program: Monthly Expense Calculator
Description:
This program calculates the total monthly expenses and remaining
savings based on user input for salary, rent, food, and travel expenses.
"""
Monthly_Salary = int(input("Enter Monthly Salary: "))
Rent = int(input("Enter Rent: "))
Food_Expenses = int(input("Enter Food Expenses: "))
Travel_Expenses = int(input("Enter Travel Expenses: "))
Total_expenses = Rent+Food_Expenses+Travel_Expenses
Remaining_Savings = Monthly_Salary - Total_expenses
print(f"Total Expenses:{Total_expenses}")
print(f"Remaining Savings: {Remaining_Savings}")