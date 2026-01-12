# """
# Day 3 – Python Conditional Statements
# Difficulty: Hard
# Program: Income Tax Calculator
#
# Description:
# Interactive Income Tax Calculator
# with user-friendly messages and slab-wise tax logic
# This program calculates income tax based on annual salary
# using slab-wise tax rules and conditional statements.

# Slab	Income Range	Tax %
# Slab 1	0 – 2,50,000	0%
# Slab 2	2,50,001 – 5,00,000	5%
# Slab 3	5,00,001 – 10,00,000	20%
# """
print("Hey! Welcome to Salary Calculator\n"
      "Here! You can calculate your Annual salary after Tax deductions.\n"
      "Let's Goooo......\n"
      "Enter your Salary and we will calculate tax deductions based on slabs.\n"
      "we will display your Exact salary after tax")
name = input("What is your name? ")
annual_salary = int(input("Enter annual salary: "))
if annual_salary <= 0:
    print("Please enter a valid annual salary")
elif annual_salary <= 250000:
    Tax_deduction = 0
    net_income = annual_salary - Tax_deduction
    print(f"Holaaa! {name} your Total Tax  :{Tax_deduction}.\nYour net Annual salary after tax deductions:{net_income:,}")
elif 250000 < annual_salary <=500000:
    Tax_deduction = (((annual_salary-250000)*5)/100)
    net_income = annual_salary - Tax_deduction
    print(f"Holaaa! {name} your Total Tax  :{Tax_deduction}.\nYour net Annual salary after tax deductions:{net_income:,}")
elif 500000 <annual_salary <=1000000:
    Tax_deduction = ( (((500000-250000)*5)/100) + (((annual_salary-500000)*20)/100) )
    net_income = annual_salary - Tax_deduction
    print(f"Holaaa! {name} your Total Tax  :{Tax_deduction}.\nYour net Annual salary after tax deductions:{net_income:,}")
else:
    Tax_deduction = (((500000-250000)*5)/100)+(((1000000-500000)*20)/100) + (((annual_salary-1000000)*30)/100)
    net_income = annual_salary - Tax_deduction
    print(f"Holaaa! {name} your Total Tax  :{Tax_deduction}.\nYour net Annual salary after tax deductions:{net_income:,}")
