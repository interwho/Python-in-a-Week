#Ex8.py
#
#Variables:
#m1 - integer 1
#m2 - integer 2
#inp - Temp. Reset Variable
#
#Input: 2 Integers
#Output: Comparison
#Process: Get data > verify > calculate > print output

import sys #Import required system resources (for exit)

def repcard() : #Function to get and verify the data
    m1 = raw_input('Enter the first integer:\n') #get input
    m2 = raw_input('Enter the second integer:\n')
    try : #error catching
        m1 = int(m1) #change types
        m2 = int(m2)
        cardout(m1,m2)
    except ValueError : #error
        print 'Invalid Number(s) - Please Try Again' #Errors
    repcard() #reset
    

def cardout(m1,m2) : #Function to actually draw the box of "X"es
    if m1 > m2 : #1 > 2
        print "Number 1 is greater than Number 2." #print output
    elif m1 < m2 : #2 > 1
        print "Number 2 is greater than Number 1." #print output
    else : #1=2
        print "The numbers are equal." #print output
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        repcard() #try again
    else :
        sys.exit() #exit

repcard() #Initialize Program
