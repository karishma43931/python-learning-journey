"""
Day 3 – Python Conditional Statements
Difficulty: Easy
Program: Voting Age Eligibility Check

Description:
This program checks whether a user is eligible to vote based
on their age. A person is eligible if the age is 18 or above.
"""
age = int(input("Enter Your Age :"))
if age>=18:
    print(f"As Your {age}Years Old,Your Eligible to Vote")
elif age<18:
    print(f"Since Your {age} Years Old,"
          f"\nYour Not Eligible to Vote."
          f"\nHe/She should be 18 years Or Greater to get the Eligibility ")

