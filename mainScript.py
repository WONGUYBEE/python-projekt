# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:00:07 2017

@author: mb-fa
"""
        #All variables within the optional functions have a number ahead. that number indicates where
        #the variable is defined
#inbuild functions
import pandas as pd
import numpy as np

#main functions
from loadData import loadData
from dataStats import dataStatistics
from bacteriaPlot import grwtTemp
from bacteriaPlot import bactTypes
from bacteriaPlot import dataPlot
from filterData import filterData

#secondary functions: inputIntNumber() or inputFloatNumber()
from inputNumber import inputIntNumber

print("Welcome to The Best Bacteria Analysis Tool - TBBAT")

#Creates a menu where user inputs value between 1-5 and gets the following options
data = None

while(True):
    print("""Your options are:
    1) Load new data
    2) Filter
    3) Display statistics
    4) Generate plots
    5) Terminate
    """)
    
    ch = inputIntNumber("Choose one of the above options")

    if(ch == 1): #calls data  and errorhandling-function
          data = loadData(filename = input("Specify your datafile.txt or press 0 for main menu: "))
          data0 = data #creates an extra backup- of the original data uploaded. 
    elif(ch in [2,3,4] and data == None):
        print("Please load some data first")
    elif(ch == 2): #calls filter data interface
          data = filterData(data, data0)
    elif(ch == 3): #calls diagram interface
          dataStatistics(data)
    elif(ch == 4): #calls show-makr interface
          dataPlot(data)
    elif(ch == 5): #terminate
          print("Goodbye.")
          break
    else:
        print("Enter valid statement")