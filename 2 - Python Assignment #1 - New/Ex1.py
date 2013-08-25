#Ex1.py
#
#Variables:
#name - name of the item
#price - price of the item
#tax - HST
#full - Full Price + HST
#inp - Temp. Reset Variable
#
#Input: Name and price of an item
#Output: Name, Price, HST, and Total Price of an item
#Process: Get data > verify > calculate > round final answers > print output

import sys #Import required system resources (for exit)

def taxcalc() : #Function to get and verify the input number
    name = raw_input('Enter the name of the item:\n') #Get data
    price = raw_input('Enter the price of the item:\n')
    try : #error catching
        price = float(price) #verification
        name = str(name)
        calctax(name,price)
    except ValueError : #error
        print 'Invalid Number - Please Try Again.' #Errors
    taxcalc() #reset
    

def calctax(name,price) : #Function to actually do the work
    tax = 0.13 * price #calculate tax
    full = price + tax #calc. full price
    tax = round(tax, 2) #round numbers
    full = round(full, 2) #round numbers
    price = round(price, 2) #round numbers
    print "Tax Calculator Program" #Print output
    print "Item: " + str(name)
    print "Price: $" + str(price)
    print "HST: $" + str(tax)
    print "Total: $" + str(full)
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        taxcalc() #try again
    else :
        sys.exit() #exit

taxcalc() #Initialize Program
