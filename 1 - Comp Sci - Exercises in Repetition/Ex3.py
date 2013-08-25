import math #Import math functions (square root)
import sys #Import system functions (exit)

def numsqr() : #Main program function
    num = raw_input('Enter a number to see if it is a perfect square:\n') #ask for input
    if num.isdigit() : #Verify that number is actually a number
        num = int(num)
        num = math.sqrt(num) #Square root number
        numb = num
        num = str(num) + 'E'
        if '.0E' in num : #Verify that number is perfect or not
            print 'That number is a perfect square (' + str(int(numb)) + ').' #print result if perfect
            inp = raw_input('Try again? (yes/no)\n') #asks user if they want to try again
            if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
                numsqr() #try again
            else :
                sys.exit() #exit
        else :
            print 'That number is NOT a perfect square (' + str(numb) + '). Please try again.' #not a perfect square
            numsqr() #restart
    else :
        print "Error - That is not a valid number. Please try again." #invalid input error
        numsqr() #restart

numsqr() #Initialize Program
