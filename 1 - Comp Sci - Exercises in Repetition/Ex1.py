import sys #Import required system resources (for exit)

def sqrrs() : #Function to get and verify the input number
    box = raw_input('Enter the length (in a full number) of the box of Xes you want to create:\n')
    if box.isdigit() : #Verification (is a number)
        if int(box) < int(51) : #Verification (is less than 51)
            sqrr(box)
        print 'There is a limit of 50 Xes per box, plese try again.' #Errors
        sqrrs()
    print 'Full numbers only, please try again.' #Errors
    sqrrs()
    

def sqrr(box) : #Function to actually draw the box of "X"es
    box = int(box)
    boxf = box
    line1 = ''
    while boxf > 0 : #generate the first line of "X"es
        boxf = boxf-1
        line1 = line1+'X'
    while box > 0 : #print the first line of "X"es times the input number
        box = box-1
        print line1
    inp = raw_input('\n\nTry again? (yes/no)\n') #Asks the user if they want to try again
    if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
        sqrrs() #try again
    else :
        sys.exit() #exit

sqrrs() #Initialize Program
