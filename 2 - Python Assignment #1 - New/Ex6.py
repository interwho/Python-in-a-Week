#Ex6.py
#
#Variables:
#m1 - length of first side
#m2 - length of second side
#a2 - 1 side squared
#b2 - 2 side squared
#h2 - hypotenuse squared
#inp - Temp. Reset Variable
#
#Input: 2 sides of a triangle
#Output: Hypotenuse
#Process: Get data > verify > calculate > print output

import sys #Import required system resources (for exit)

def repcard() : #Function to get and verify the data
    m1 = raw_input('Enter the length of the 1st side:\n') #get data
    m2 = raw_input('Enter the length of the 2nd side:\n')
    try : #error catching
        m1 = float(m1) #convert data
        m2 = float(m2)
        cardout(m1,m2)
    except ValueError : #error
        print 'Invalid Number(s) - Please Try Again' #Errors
    repcard() #reset
    

def cardout(m1,m2) : #Function to actually calculate
    a2 = m1*m1 #calculate squares of each side
    b2 = m2*m2
    h2 = a2 + b2
    print "Hypotenuse: " + str(h2) + " = " + str(a2) + " + " + str(b2) #print results
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        repcard() #try again
    else :
        sys.exit() #exit

repcard() #Initialize Program
