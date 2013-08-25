#Ex3.py
#
#Variables:
#seconds - input number
#remain - remaining time
#days - total days
#hours - total hours
#minutes - total minutes
#seconds - total seconds
#inp - Temp. Reset Variable
#
#Input: # of seconds after midnight
#Output: Time in format - d : h : m : s
#Process: Get data > verify > calculate > round final answers > print output

import sys #Import required system resources (for exit)

def start() : #Function to get and verify the data
    seconds = raw_input('Enter the number of seconds after midnight:\n') #get input
    try : #Verify data
        seconds = int(seconds) #convert inputs
        datetime(seconds) #call function
    except ValueError : #error
        print 'Invalid Number - Please Try Again' #Errors
    start() #reset
    

def datetime(seconds) : #Function to actually print the results
    remain = seconds #set initial variables
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    while remain > 86400 or remain == 86400 : #calculate days
        days = days+1
        remain = remain - 86400
    while remain > 3600 or remain == 3600 : #calculate hours
        hours = hours+1
        remain = remain - 3600
    while remain > 60 or remain == 60 : #calculate minutes
        minutes = minutes+1
        remain = remain - 60
    seconds = remain #calculate seconds
    print str(days) + " : " + str(hours) + " : " + str(minutes) + " : " + str(seconds) #print results
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        start() #try again
    else :
        sys.exit() #exit

start() #Initialize Program
