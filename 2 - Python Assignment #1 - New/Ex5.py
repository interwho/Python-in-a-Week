#Ex5.py
#
#Variables:
#marks - mark array
#verif - verification variable
#ver - verification veriable
#totalmarks - sum
#marksn - avg
#classavg - final avg
#inp - Temp. Reset Variable
#
#Input: Numbers
#Output: Sum and average of those numbers
#Process: Get data > verify > split > calculate > round final answers > print output

import sys #Import required system resources (for exit)

def marksc() : #Function to get and verify the input
    marks = raw_input("Please enter a series of numbers that you would like to sum and average, separated by commas (,):\n") #Ask for user input
    verif = "||" + marks + "||" #verify
    if "||," in verif :
        print "Invalid Format - Please Try Again!" #improper formatting error
        marksc() #reset
    if ",||" in verif : #verify
        print "Invalid Format - Please Try Again!" #empty array error
        marksc() #reset
    if "," in marks :
        ver = marks.split(',') #format error check
        for mark in ver:
            try :
                float(mark) #error check
            except ValueError :
                print "Invalid Format - Please Try Again!" #error
                marksc() #reset
        markcalc(marks) #Successful, now calculate
    else :
        print "Invalid Format - Please Try Again!" #error
        marksc() #reset
    

def markcalc(marks) : #Function to do the calculating
    marks = marks.split(',') #Split the data into an array (list) by comma
    totalmarks = 0 #set initial variable
    marksn = len(marks) #get total number of numbers
    for mark in marks: #Count sum
        mark = float(mark)
        totalmarks = totalmarks + mark
    classavg = totalmarks / marksn #Calculate average
    print "Sum of the numbers: " + str(totalmarks) #Print results
    print "Average of the numbers: " + str(classavg)
    inp = raw_input('\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        marksc() #try again
    else :
        sys.exit() #exit

marksc() #Initialize Program
