"""
Day 3 – Python Conditional Statements
Difficulty: Medium
Program: ATM Withdrawal Validation

Description:
This program validates an ATM withdrawal request by checking
withdrawal amount conditions and available account balance.
"""

Account_blance = int(input("Enter your Account Balance : "))
Withdrawl_amount = int(input("Enter your Withdrawl Amount : "))
Balance = Account_blance - Withdrawl_amount
if (Withdrawl_amount%100 ==0) and (Withdrawl_amount<=Account_blance):
    print(f"Processing Your Withdrawl Amount: {Withdrawl_amount} \nYour Remaining Balance: {Balance} ")
elif (Withdrawl_amount%100 ==0) and (Withdrawl_amount>Account_blance):
    print("Insufficient Balance")
else:
    print("Enter amount in multiples of 100")