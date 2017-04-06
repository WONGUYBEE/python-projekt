# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 08:53:32 2017
@author: mb-fa
"""
import os
import stat
import pandas as pd
import numpy as np
import stat
                            #Funktionen importerer data og tjekker og fjerner fejl. 
                            # det første while loop importerer data
def loadData(filename):         
    while True:
        try:
            if(filename == "0"):    #optional return to main menu
                break
                
            data = pd.read_csv(filename, sep='\s+',header=None) #reads the file
            break          #Continues to errorhandling
            
        except:   
            try:
                if(os.stat(filename).st_size == 0):   #checks if file is empty
                  print("Your file is empty, please select another one")        
                
            except: #shows the user, all the available files in the directory
                print("No such file in directory. your current directory is:", os.getcwd())
                print("Files available is", os.listdir())
                filename = input("\nWrite the name of your datafile or 1 for return to main menu:")
            
                                    #I funktionen nedenfor tjekkes om et stykke data i kolonne j og række i, er indenfor en given range for         
                                    #adds data to arrays
    if(filename != "1"):                      
        temperature = np.array(data[0]) # mellem 10 og 60
        growthrate = np.array(data[1])  # positivt tal
        bacteria = np.array(data[2])    # 1,2,3,4  
        
        e = np.zeros(0)                 #creates an array for errored lines, further down the number of the line(s) with errors will be appended to this array. 
        
        i1 = 0                          #counts numbers of errors
        i2 = 0
        i3 = 0   
        print(data)     
        for j in range(3):        
            for i in range(np.size(data[j])):
                if  j == 0 and temperature[i] > 60 or temperature[i] < 10 :                              #chcking if within range
                    print("Temperature in measurement", i+1, "is not in range 10-60C, but:", temperature[i])
                    i1 = i1+1                                                                           #counting errornumbers
                    e = np.append(e,[i])                                                                #adding errorline-position to array
                elif j == 1 and growthrate[i] <= 0:
                    print(temperature[i])
                    print("GrowthRate in measurement", i+1, "is not a positive number, but:", growthrate[i])
                    i2 = i2+1
                    e = np.append(e,[i])
                elif j == 2 and (bacteria[i] not in [1,2,3,4]):
                    print("BacteriaType in measurement", i+1, "is not in range [1..4], but:", bacteria[i])
                    i3 = i3+1
                    e = np.append(e,[i])
        
        e = np.unique(e)                                     #removing doublicates of errored lines
                        
        data = np.delete(np.array(data.iloc[:,:]),e,0)   #removing invalid datalines
        
        #printing ending statement
        
        print("\nTemperature has:", i1, "errors |", "Growthrate has:", i2, "errors |", "Bacteriatype has:", i3, "errors", "| total errors:", i1+i2+i3)
        print("Total lines removed were:", len(e) , "| The measurement(s) removed were:", e+1)
        print("Data has been filtered & loaded")

    return(data)
