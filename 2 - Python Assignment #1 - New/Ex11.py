#Ex11.py
#
#Variables:
#q - Question in human-text
#ans - answer to the question
#tries - # of tries used so far
#method - +,- or x
#num1 - number 1 in equation
#num2 - number 2 in equation
#inp - Temp. Reset Variable
#
#Input: Answer to question
#Output: Whether correct or not
#Process: Generate question > print question > Get answer > verify > check > print output > loop

import sys #Import required system resources (for exit)
import random #import the random number generator

def getans(q,ans,tries) : #question function
    uans = raw_input(q) #get the user's answer
    try : #catch errors
        uans = int(uans) #convert user answer
        if ans != uans : #if incorrect
            print "Incorrect. Please Try Again." #error
            tries = tries + 1 #+1 try
            getans(q,ans,tries) #reloop
        else :
            print "Correct!" #correct!
            print "That took " + str(tries) + " tries!" #print number of tries
            inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
            if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
                startGame() #try again
            else :
                sys.exit() #exit
    except ValueError : #error
        print "Incorrect. Please Try Again." #error message
        tries = tries + 1 #+1 try
        getans(q,ans,tries) #reloop


def startGame() : #game question generator
    method = random.randint(1,3) #generate a random equation type (x,-,+)
    if method == 3 : #+
        num1 = random.randint(1,1000) #number 1
        num2 = random.randint(1,1000) #number 2
        ans = num1 + num2 #answer
        q = str(num1) + " + " + str(num2) + " = " #generate the question
        getans(q,ans,1) #call question function
    elif method == 2 : #-
        num1 = random.randint(1,1000) #number 1
        num2 = random.randint(1,1000) #number 2
        ans = num1 - num2 #answer
        q = str(num1) + " - " + str(num2) + " = " #generate the question
        getans(q,ans,1) #call question function
    elif method == 1 : #x
        num1 = random.randint(1,1000) #number 1
        num2 = random.randint(1,1000) #number 2
        ans = num1 * num2 #answer
        q = str(num1) + " x " + str(num2) + " = " #generate the question
        getans(q,ans,1) #call question function

print "Math Game" #print title
startGame() #start program
