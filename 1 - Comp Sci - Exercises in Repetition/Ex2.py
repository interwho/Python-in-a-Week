import sys #Import required system resources (for exit)

def marksc() : #Function to get and verify the input
    marks = raw_input('Please enter all your students marks, with each separated by a comma (,):\n') #Ask for user input
    verif = "||" + marks + "||"
    if "||," in verif :
        print "Invalid Format - Please Try Again!" #improper formatting error
        marksc()
    if ",||" in verif :
        print "Invalid Format - Please Try Again!" #empty array error
        marksc()
    if "," in marks :
        ver = marks.split(',') #format error check
        for mark in ver:
            try :
                float(mark) #error check
            except ValueError :
                print "Invalid Format - Please Try Again!" #error
                marksc()
        markcalc(marks) #Successful, now calculate
    else :
        print "Invalid Format - Please Try Again!" #error
        marksc()
    

def markcalc(marks) : #Function to do the calculating
    marks = marks.split(',') #Split the data into an array (list) by comma
    i = 0
    totalmarks = 0
    marksn = len(marks)
    for mark in marks: #Count number of marks, sum, and fails
        mark = float(mark)
        totalmarks = totalmarks + mark
        if mark < 50 : #Calculate number of people failing
            i = i + 1
    classavg = totalmarks / marksn #Calculate average
    print "Num of people failing the year: " + str(i) #Print results
    print "Class average: " + str(classavg) + "%"
    inp = raw_input('\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        marksc() #try again
    else :
        sys.exit() #exit

marksc() #Initialize Program
