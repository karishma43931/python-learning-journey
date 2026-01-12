"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: FizzBuzz

Description:
This program checks whether a number is divisible by 3, 5,
or both, and prints Fizz, Buzz, or FizzBuzz accordingly.
"""
y = int(input("Enter a number : "))
if y%3==0 and y%5==0:
    print("FizzBuzz")
elif y%3==0 and y%5!=0:
    print("Fizz")
elif y%3!=0 and y%5==0:
    print("Buzz")
elif y%3!=0 and y%5!=0:
    print("Not divisable by 3 or 5")