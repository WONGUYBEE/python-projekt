# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:36:55 2017

@author: mb-fa
"""

import pandas as pd
import numpy as np
from inputNumber import inputIntNumber
from inputNumber import inputFloatNumber

def filterData(data, data0):     
    
    dataTypeMenu = "Choose which datatype you want to apply a filter to \n1 = Temperature \n2 = Growthrate \n3 = Bacteriatype'\n4 = Reset \n5 = Show data \n0 For return to main menu."
    bacteriaString = "Choose which bacteriatype you want filter for \n1 = Salmonella enterica \n2 = Bacillus cereus \n3 = Listeria \n4 = Brochothrix thermosphacta \n0 = return"
    upLim = "Insert your upper-limit T < u.limit, as a number [e.g. 3.45]"
    lowLim = "Insert your lower-limit T > l.limit, as a number [e.g. 3.45]"
    limitMenu = "1 for lowerLimitation \n2 for upperlimitation \n3 for between two limits\n 0 to return to main menu"
    bacList = np.array([0, "Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])

    while True:          
        mainC = inputIntNumber(dataTypeMenu)
    
        if(mainC == 0): #returns to main menu
            print("The size of samples after filtering is: {:d} | Total samples filtered out are {:d}".format(len(data),(len(data0)-len(data)))) #prints number of current and removed samples
            break
        
        if(mainC == 1): #sorts for temperature  
              while True:
                  print("To sort for temperature, you must now specify filtering limits" )
                  limitType = inputIntNumber(limitMenu) #allows the user to choose specific limitations for samples
                  
                  if(limitType == 0):  
                      break
                  
                  if(limitType == 1):  
                      data = data[data[:,0]>inputFloatNumber(lowLim)]
                      print("Limit has been set")
                      break
                      
                  if(limitType == 2):
                      data = data[data[:,0]<inputFloatNumber(upLim)]
                      print("Limit has been set")
                      break
                  
                  if(limitType == 3):
                      data = data[data[:,1]<inputFloatNumber(upLim)]
                      data = data[data[:,1]>inputFloatNumber(lowLim)]
                      print("Temperature - limit has been set")
                      break
                  
              
        if(mainC == 2): #sorts for growthrate
              while True:
                  print("To sorts for GrowthRate, you must now specify filtering limits" )
                  limitType = inputIntNumber(limitMenu) #allows the user to choose specific limitations for samples
                  
                  if(limitType == 0):  
                      break
                  
                  if(limitType == 1):  
                      data = data[data[:,1]>inputFloatNumber(lowLim)]
                      print("Growthrate limit has been set")
                      break
                      
                  if(limitType == 2):
                      ul = inputFloatNumber(upLim)
                      data = data[data[:,1]<ul]
                      print("Growthrate limit has been set")
                      break
                  if(limitType == 3):

                      data = data[data[:,1]<inputFloatNumber(upLim)]
                      data = data[data[:,1]>inputFloatNumber(lowLim)]
                      print("Growthrate limit has been set")
                      break
 
        if(mainC == 3):  #sorts for bacteria type
            while True: #we are here checking is numbers (types) is within a given range [1..4] or 0 for return
                bacType = inputIntNumber(bacteriaString)
                if(bacType in [0, 1, 2, 3, 4]):
                    if(bacType in [1, 2, 3, 4]):
                        data = data[data[:,2]==bacType]  #sorts for the specific type, which is given in bacType
                        print("Data has been filtered for:", bacList[bacType])
                    break
                else:
                    print("\nPlease enter a valid statement")
                    
        if(mainC == 4): #resets data
            data = data0
            
        if(mainC == 5): #prints data
            print("Current data is left with the implemented filters:")
            print(data)
    
    return(data)
