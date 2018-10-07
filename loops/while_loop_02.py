#! /usr/bin/env python3
"""Calculates sum of user entered integers in a while loop
"""

status = "go"
sum = 0
while status != "stop":
    sum = sum + int(input("Enter number to be added to sum: "))
    status = input("To finished adding enter stop: ")
print("The total is " + str(sum))
