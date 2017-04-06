#importing numpy as i need this library
import numpy as np

#secondary functions: inputIntNumber() or inputFloatNumber()
from inputNumber import inputIntNumber

def dataStatistics(data):
    #Displaying the menu
    print("""Welcome to Data Statistics function!
    You now have the following options
    1) If you entered the function by accident, press 1 to return to the menu
    2) Show the mean temperature
    3) Show the mean growth rate
    4) Show the standard deviation of temperature
    5) Show the standard deviation of growth rate
    6) Show the total number of rows in  the data
    7) Show the mean growth rate when the temperature is below 20 C.
    8) Show the mean growth rate when the temperature is above 50 C.
    """)
    
    #creating the varibale we use to store the user input
#    choice=0
    
    #starting a loop that makes it possible for the user to pick from the menu
    while True: 
        choice = inputIntNumber("Choose one of the options above ")
        
        #this makes a "break" for the program, and puts the user back into the menu
        if  choice==1:
            break
        
        #from here and down we refer to a function further down, that we then use to do whatever we want to do
        elif choice==2:
            meanTemp(data)
            break
                
        elif choice==3:
            meanGrwt(data)
            break
            
        elif choice==4:
            stdTemp(data)
            break
            
        elif choice==5:            
            stdGrwt(data)
            break
            
        elif choice==6:
            rows(data)
            break
            
        elif choice==7:
            meanCold(data)
            break
            
        elif choice==8:            
            meanWarm(data)
            break
            
        #this else makes sure we use a meaningful input, as everything that isnt a number from 1-8 will send the user right back
        else:
            print("Enter valid statement")
        
    #printing the mean from the first row. The ":" means entire row.
def meanTemp(data):
    print(data[:,0].mean())
    
    #printing the mean from the second row
def meanGrwt(data):
    print(data[:,1].mean())
    
    #printing the std of data in the first row
def stdTemp(data):
    print(np.std(data[:,0]))
    
    #printing the std of data in the second row 
def stdGrwt(data):
    print(np.std(data[:,1]))
    
    #a built in function that counts the rows
def rows(data):
    print(len(data))
    
    #takes the mean of the second column of data, for the rows that have a number below 20 in the first column
def meanCold(data):
    print(np.mean(data[:,1][data[:,0]<20]))
    
    #takes the mean of the second column of data, for the rows that have a number above 50 in the first column
def meanWarm(data):
    print(np.mean(data[:,1][data[:,0]>50]))

