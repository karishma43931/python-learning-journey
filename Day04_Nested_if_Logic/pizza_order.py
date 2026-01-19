"""
Day 4 – Python Conditional Statements & Input Validation
Difficulty: Easy–Medium
Program: Pizza Delivery Billing System

Description:
Develop an interactive pizza ordering program that calculates
the total bill based on the selected pizza size and optional
toppings such as pepperoni and extra cheese. The program must
validate mandatory inputs, handle optional choices correctly,
and display the final bill only when all user inputs are valid.
"""
print("Welcome to pizza delivery store")
bill = 0
valid_order = True
size = input("What size pizza do you want?\nSmall,Medium,Large: ").lower()
pepperoni = input("Do you have pepperoni? on your pizza.\nYes or No: ").lower()
extra_cheese = input("Do you have extra cheese? on your pizza.\nYes or No: ").lower()
if (size != "small") and  (size != "medium") and  (size != "large" ):
    print("Sorry, I don't understand your input.\nWe cannot proceed your order... without valid size")
    valid_order = False
else :
    if size == "small":
        bill += 120
    elif size == "medium":
        bill += 200
    elif size == "large":
        bill += 300

    if pepperoni == "yes":
        if size == "small":
            bill += 10
        else:
            bill += 20
    elif pepperoni == "no":
        bill+=0
    else:
        print('Sorry! Want to add pepperoni,\nplease select "yes" or "no"')
        valid_order = False

    if extra_cheese == "yes":
        if size == "small":
            bill += 10
        else:
            bill += 20
    elif extra_cheese == "no":
        bill+=0
    else:
        print('Sorry! Do you need extra cheese \nplease select "yes" or "no" to proceed')
        valid_order = False

    if valid_order:
        print(f"Your Total bill is {bill}")






