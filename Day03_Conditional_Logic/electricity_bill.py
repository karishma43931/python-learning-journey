"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: Electricity Bill Calculation

Description:
This program calculates the electricity bill amount based on
the number of units consumed using slab-wise billing logic.
"""
no_of_units = int(input("Enter a number of Units Consumed : "))
if no_of_units<=0:
    print("Invalid Input")
elif (no_of_units >0 and no_of_units <=100):
    print(f"Since Your CurrentBill or Units consumed is less than 100,Total Bill is RS.0")
elif no_of_units >100 and no_of_units <=200:
    print(f"You`ve Consumed : {no_of_units} units and \nyour Total CurrentBill to Pay for this Month will be :{((100*0) + (no_of_units-100)*5)} ")
else:
    print(f"Youve Consumed :{no_of_units} units and \nYour Totall CurrentBill to Pay this month will be :{((100*0) + (100*5) + ((no_of_units-200)*10))} ")
