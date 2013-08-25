#Ex9.py
#
#Variables:
#marks - input
#verif - verification variable
#ver - verification variable
#mark - in-loop variable
#largest - largest number
#inp - Temp. Reset Variable
#
#Input: Series of numbers
#Output: Largest number
#Process: Get data > verify > calculate > print output

import sys #Import required system resources (for exit)

def marksc() : #Function to get and verify the input
    marks = raw_input("Please enter a series of numbers that you would like to compare, separated by commas (,):\n") #Ask for user input
    verif = "||" + marks + "||"
    if "||," in verif :
        print "Invalid Format - Please Try Again!" #improper formatting error
        marksc()
    if ",||" in verif :
        print "Invalid Format - Please Try Again!" #empty array error
        marksc()
    if "," in marks :
        ver = marks.split(',') #format error check
        for mark in ver: #check each variable in array
            try : #error checking
                float(mark) #error check
            except ValueError : #error
                print "Invalid Format - Please Try Again!" #error
                marksc() #reset
        markcalc(marks) #Successful, now calculate
    else :
        print "Invalid Format - Please Try Again!" #error
        marksc() #reset
    

def markcalc(marks) : #Function to do the calculating
    marks = marks.split(',') #Split the data into an array (list) by comma
    largest = 0 #initial variable
    for mark in marks: #Get largest
        mark = float(mark) #convert type
        if mark > largest : #is this number the largest
            largest = mark
    print "Largest Number: " + str(largest) #print output
    inp = raw_input('\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        marksc() #try again
    else :
        sys.exit() #exit

marksc() #Initialize Program
