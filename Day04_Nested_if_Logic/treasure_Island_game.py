"""
Day 4 – Python Conditional Statements
Difficulty: Easy
Program: Treasure Island – Text-Based Adventure Game

Description:
Create a simple text-based adventure game where the user
navigates through multiple choices to find the treasure.
The program should use nested conditional statements to
control the game flow and determine winning or losing paths.
User input should be handled in a case-insensitive manner,
and clear messages should be displayed for each outcome.
"""
treasure_art = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
print(treasure_art)
print("Welcome to treasure island!")
print("Your mission is to find Treasure island.")
choice = input("Choose Left or Right: ").lower()

if choice == "left":
    choice1 = input(' "swim" or "wait" ').lower()

    if choice1 == "wait":
        choice2 = input('Which door u want to open:'
                         'Choose door:"Red" or "Blue" or "Yellow" :').lower()

        if choice2 == "red":
            print("Attacked by beast")
        elif choice2 == "blue":
            print("Room full of Fire")
        elif choice2 == "yellow":
            print("🎉 YAY! You found the treasure. You Win!")
        else:
            print("Invalid Input! Game over!")

    else:
        print("Eaten by trout")

else:
    print("You Fell into a hole.Game Over")
