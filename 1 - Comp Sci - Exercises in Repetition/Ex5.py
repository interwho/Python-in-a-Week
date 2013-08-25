import sys #Import required system resources (exit)

def factorst() : #Input retreival and verification function
        num = raw_input("Enter a whole number to find all of it's factors:\n") #Get user input
        if num.isdigit() : #is input a number?
                try :
                        num = int(num)
                        factorit(num) #no errors, begin factor calculation function
                except ValueError :
                        print "Invalid Number - Please Try Again" #error
                        factorst() #restart
        print "Invalid Number - Please Try Again" #error
        factorst() #restart

def factorit(num) : #Factor calculation function
        print "Factors of " + str(num) + " are:" #Print results
        stnum = num
        while num > 0 : #Calculate each factor
                n = float(stnum)/float(num)
                b = n
                b = str(b) + "||"
                if ".0||" in b : #Are they whole numbers?
                        print int(n) #Print them
                num = int(num) - 1
        inp = raw_input('\nTry again? (yes/no)\n') #Ask user if they want to try again
        if inp == 'yes' or inp == 'Yes' or inp == 'YES' or inp == 'y' or inp == 'Y' :
                factorst() #restart program
        else :
                sys.exit() #exit

factorst() #Initialize Program
