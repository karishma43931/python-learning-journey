"""
Program Name: Star Triangle Pattern
Difficulty Level: Medium

Problem Statement:
How can we print a right-angled triangle pattern of stars (*)
in Python based on user input?

Description:
The program takes a number 'n' from the user and prints a
triangle pattern with 'n' rows. Each row contains an
increasing number of stars, forming a right-angled triangle.

Example:
Input: 5
Output:
*
* *
* * *
* * * *
* * * * *
"""
n = int(input("enter a number:"))
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print("*")
