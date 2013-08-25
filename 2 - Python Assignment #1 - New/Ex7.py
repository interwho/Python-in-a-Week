#Ex7.py
#
#Variables:
#m1 - input
#ans - answer
#inp - Temp. Reset Variable
#
#Input: Positive Integer
#Output: Factorial of that number
#Process: Get data > verify > calculate > print output

import sys #Import required system resources (for exit)

def repcard() : #Function to get and verify the data
    m1 = raw_input('Enter the number you want to find the factorial for:\n') #input
    try : #error checking
        m1 = int(m1) #convert type
        cardout(m1) #start calculating
    except ValueError : #error
        print 'Invalid Number(s) - Please Try Again' #Errors
    repcard() #reset
    

def cardout(m1) : #Function to actually calculate
    ans = 1 #initial answer
    while m1 > int(0) : #calc loop
        ans = ans*m1 #calculate
        m1 = m1-1
    print "The factorial of that number is: " + str(ans) #print output
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        repcard() #try again
    else :
        sys.exit() #exit

repcard() #Initialize Program
