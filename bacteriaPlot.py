#importing relevant libraires
import numpy as np
import matplotlib.pyplot as plt

#secondary functions: inputIntNumber() or inputFloatNumber()
from inputNumber import inputIntNumber



#starts the function
def dataPlot(data):
    #printing the menu
    print("""Welcome to Dataplotting function!
    You now have the following options:
    1) If you entered the function by accident, press 1 to return to the menu
    2) Plot the number of each of the different types of bacteria
    3) Plot the growthrate by temperature
    """)
    
    #choice=0
    #starts the menu loop
    while True:
        #uses the function "inputIntNumber" that we have defined elsewehere.
        #puts the user back into the loop in case of a value error
        choice = inputIntNumber("Choose one of the options above: ")
        
        #Stops the program from running
        if  choice==1:
            break
        
        #selects the functions defined below
        elif choice==2:
            bactTypes(data)
            break
                
        elif choice==3:
            grwtTemp(data)
            break
        
        #makes sure that anything that isn't a number between 0 and 3 stops puts the user back into the loop
        else:
            print("Enter valid statement")

#Defines the first function        
def bactTypes(data):
    #Sorts the data from lowest to highest from the first coloumn
    sorteret=data[np.argsort(data[:,0])]

    #sorts from the types in third column. The rows are still in sorted from highest to lowest aswell
    a=sorteret[sorteret[:,2]==1]
    b=sorteret[sorteret[:,2]==2]
    c=sorteret[sorteret[:,2]==3]
    d=sorteret[sorteret[:,2]==4]
    
    #defines what we want to plot
    #first i'm telling the progam what data it should plot from. I define
    #that as x in first row, and y in second. Aftwerwards i define a color and a label for the data
    plt.plot(a[:,0], a[:,1], color='r', label="Salmonella enterica")
    plt.plot(b[:,0], b[:,1], color='b', label="Bacillus cereus")
    plt.plot(c[:,0], c[:,1], color='g', label="Listeria")
    plt.plot(d[:,0], d[:,1], color='y', label="Brochothrix thermosphacta")
    #this puts the labels to the upper left corner
    plt.legend(loc="upper left")
    
    #Putting on the nametags for the axis
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    #Setting the limitations of the plot. The x is defined in a
    #predefined area, while the y is varies to fit the data
    plt.xlim([10, 60])
    #th
    plt.autoscale(enable=True, axis='y', tight=None)
    #Actually calling the plot
    plt.show()
    
def grwtTemp(data):
    #defines that we want four rows, and they should display data from the third row
    plt.hist(data[:,2], [1,2,3,4,5])
    plt.xticks([1.5,2.5,3.5,4.5],["Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta"])
    #naming the axis and diagram
    plt.title("Number of each type of bacteria in the data")
    plt.xlabel("Types")
    plt.ylabel("Number of bacteria")
    #defining the axies the same way as we did before
    plt.xlim([1, 5])
    plt.autoscale(enable=True, axis='y', tight=None)
    #actually calling the plot
    plt.show()
    
#dataPlot()