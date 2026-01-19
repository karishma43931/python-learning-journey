"""
Program Name: Random Password Generator
Difficulty Level: Medium

Description:
Generates a random password using letters, numbers,
and symbols based on user input.

Concepts Used:
Lists, loops, random module, join()
"""
import random

print("Welcome to Password Generator!\nTired of giving regular passwords.\nStruggling to give a different new password everytime you reset passwords/for signups. \nI`m here to give you a unique password.Give me some inputs and Tadaa I will give you some unique password")

name = input("What is your name? ")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '?', '*', '+', '-', '/', '=', '@', '#', '$', '%', '^', '&', '*', '(', ')']
password_list = []
letters = int(input('Enter no of  letters you want in your password: '))
numbers = int(input('Enter no of  numbers you want in your password: '))
symbols = int(input('Enter no of  symbols you want in your password: '))

for i in range(0, letters):
    password_list.append(random.choice(alphabets))

for i in range(0,numbers):
    password_list.append(random.choice(num))

for i in range(0,symbols):
    password_list.append(random.choice(characters))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = "".join(password_list)
print(f"Hey {name}! Here is your unique password:\n{password}")