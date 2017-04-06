# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:41:01 2017

@author: mb-fa
"""

#these two functions allows for inputs of numbers as float or integers, and returns error-statement if answer is not within expected type

def inputIntNumber(givenInput):
    while True:
        try:
            print(givenInput)
            userInput = input("Insert here: ")
            intNum = int(userInput)
            break
        except ValueError:
            print("\nEnter valid statement ")
            
    return(intNum)
        
def inputFloatNumber(givenInput):
    while True:
        try:
            print(givenInput)
            userInput = input("Insert here: ")
            floatNum = float(userInput)
            break
        except ValueError:
            print("\nEnter valid statement ")
    return(floatNum)
