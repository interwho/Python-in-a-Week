#Ex2.py
#
#Variables:
#name - name of the student
#c1 - class 1 name
#c2 - class 2 name
#c3 - class 3 name
#c4 - class 4 name
#m1 - class 1 mark
#m2 - class 2 mark
#m3 - class 3 mark
#m4 - class 4 mark
#avg - student average
#inp - Temp. Reset Variable
#
#Input: Student name and Name and mark of that student's classes
#Output: Student report card
#Process: Get data > verify > calculate > round final answers > print output

import sys #Import required system resources (for exit)

def repcard() : #Function to get and verify the data
    name = raw_input('Enter the name of the student:\n') #get input data
    c1 = raw_input('Enter the name of their 1st class:\n')
    c2 = raw_input('Enter the name of their 2nd class:\n')
    c3 = raw_input('Enter the name of their 3rd class:\n')
    c4 = raw_input('Enter the name of their 4th class:\n')
    m1 = raw_input('Enter the mark of their 1st class:\n')
    m2 = raw_input('Enter the mark of their 2nd class:\n')
    m3 = raw_input('Enter the mark of their 3rd class:\n')
    m4 = raw_input('Enter the mark of their 4th class:\n')
    try : #error checking
        m1 = float(m1) #convert data to proper formats
        m2 = float(m2)
        m3 = float(m3)
        m4 = float(m4)
        name = str(name)
        c1 = str(c1)
        c2 = str(c2)
        c3 = str(c3)
        c4 = str(c4)
        cardout(name,c1,c2,c3,c4,m1,m2,m3,m4) #build report card
    except ValueError : #error
        print 'Invalid Number(s) - Please Try Again' #Errors
    repcard() #reset
    

def cardout(name,c1,c2,c3,c4,m1,m2,m3,m4) : #Function to actually draw the report card
    avg = m1+m2+m3+m4 #calculate average
    avg = avg/4
    avg = round(avg, 2) #round answer
    print "REPORT CARD" #print output
    print "STUDENT: " + str(name)
    print "MARKS:"
    print "     " + c1 + ": %" + str(m1)
    print "     " + c2 + ": %" + str(m2)
    print "     " + c3 + ": %" + str(m3)
    print "     " + c4 + ": %" + str(m4)
    print "TERM AVERAGE = %" + str(avg)
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        repcard() #try again
    else :
        sys.exit() #exit

repcard() #Initialize Program
