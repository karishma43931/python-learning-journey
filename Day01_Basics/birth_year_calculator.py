"""
Day 1 – Python Basics
Difficulty: Medium
Program: Birth year calculator
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_Year = int(input("Enter current Year: "))
birth_Year = current_Year - age
print(f"Hello {name},Your were born in {birth_Year}")