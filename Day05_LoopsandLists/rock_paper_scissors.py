"""
Program Name: Rock Paper Scissors Game
Difficulty Level: Easy

Description:
The program takes user input, generates a random choice for
the computer, compares both choices, and displays the result.

Concepts Used:
Lists, if-elif conditions, random module, user input
"""
import random
game = ["rock","paper","scissors"]
user_input = input("Type:rock/paper/scissors:\n").lower()
print(f"Your choice:\n {user_input}")
computer_choice = random.choice(game)
print(f"Computer choice:\n{computer_choice}")

if user_input == computer_choice:
    print("It's a Tie!Play Again..")
elif user_input == "rock" and  computer_choice== "scissors":
    print("You win!")
elif user_input == "paper" and computer_choice== "scissors":
    print("You Lose!")
elif user_input == "scissors" and computer_choice== "rock":
    print("You Lose!")
elif user_input == "scissors" and computer_choice== "paper":
    print("You Win!")
elif user_input == "paper" and computer_choice== "rock":
    print("You Win!")
elif user_input == "rock" and computer_choice== "paper":
    print("You Lose!")
else:
    print("Invalid input!")
