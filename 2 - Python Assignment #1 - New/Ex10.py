#Ex10.py
#
#Variables:
#m1 - yearly income
#total - copy of m1
#totaltax - total amount of tax that has to be paid
#inp - Temp. Reset Variable
#
#Input: income
#Output: tax that needs to be paid
#Process: Get data > verify > calculate > print output

import sys #Import required system resources (for exit)

def repcard() : #Function to get and verify the data
    m1 = raw_input('Enter your yearly income (as a full number, without the dollar sign):\n') #input
    try : #error checking
        m1 = int(m1) #convert type
        cardout(m1) #calc
    except ValueError : #error
        print 'Invalid Number(s) - Please Try Again' #Errors
    repcard() #reset


def cardout(m1) : #Function to actually draw the box of "X"es
    total = m1 #copy variable
    if m1 < int(0) : #invalid
        print 'Invalid Number(s) - Please Try Again' #Errors
        repcard() #reset
    if m1 <= 27000 and m1 >= 0 : #lowest income bracket
        totaltax = m1 * 0.17
    elif m1 <= 54500 and m1 > 27000 : #income bracket 2
    	totaltax = 27000 * 0.17
    	m1 = m1 - 27000
    	totaltax = totaltax + (m1*0.24)
    elif m1 > 54500 : #income bracket 3
    	totaltax = 27000 * 0.17
    	m1 = m1 - 27000
    	totaltax = totaltax + (27500 * 0.24)
    	m1 = m1 - 27500
    	totaltax = totaltax + (m1*0.29)
    totaltax = round(totaltax,2) #round
    print "The amount of tax you have to pay on $" + str(total) + " is: $" + str(totaltax) #print output
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        repcard() #try again
    else :
        sys.exit() #exit

repcard() #Initialize Program
