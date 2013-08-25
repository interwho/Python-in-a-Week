import sys #import required system resources (exit)
from array import * #import array methods (list)

def vote(numvote,cand1,cand2,cand3,varray,orignum) : #Voting Function
        if numvote == 0 : #Are there any votes remaining?
                print "##################################################################\n\nAnd the winner(s) is...\n" #If no, calculate winner
                n = 0
                winner = 0
                for i in varray : #Calculate each candidate's votes
                        n = n+1
                        if i > winner :
                                winner = i
                                winnum = n
                        if n == 1 :
                                one = i
                        elif n == 2 :
                                two = i
                        elif n == 3 :
                                thr = i
                if winnum == 1 : #Print the winners and their vote percentages
                        print cand1 + " with " + str(one) + " vote(s) out of " + str(orignum) + " (" + str((float(one)/float(orignum))*float(100)) + " percent)."
                elif winnum == 2 :
                        print cand2 + " with " + str(two) + " vote(s) out of " + str(orignum) + " (" + str((float(two)/float(orignum))*float(100)) + " percent)."
                elif winnum == 3 :
                        print cand3 + " with " + str(thr) + " vote(s) out of " + str(orignum) + " (" + str((float(thr)/float(orignum))*float(100)) + " percent)."
                if one == winner and winnum != 1 :
                        print cand1 + " with " + str(one) + " vote(s) out of " + str(orignum) + " (" + str((float(one)/float(orignum))*float(100)) + " percent)."
                if two == winner and winnum != 2 :
                        print cand2 + " with " + str(two) + " vote(s) out of " + str(orignum) + " (" + str((float(two)/float(orignum))*float(100)) + " percent)."
                if thr == winner and winnum != 3 :
                        print cand3 + " with " + str(thr) + " vote(s) out of " + str(orignum) + " (" + str((float(thr)/float(orignum))*float(100)) + " percent)."
                print "\nThe total vote breakdown is as follows:\n" #Print total vote breakdown
                print cand1 + " had " + str(one) + " vote(s) out of " + str(orignum) + " (" + str((float(one)/float(orignum))*float(100)) + " percent)."
                print cand2 + " had " + str(two) + " vote(s) out of " + str(orignum) + " (" + str((float(two)/float(orignum))*float(100)) + " percent)."
                print cand3 + " had " + str(thr) + " vote(s) out of " + str(orignum) + " (" + str((float(thr)/float(orignum))*float(100)) + " percent)."
                raw_input()
                sys.exit()
        num = raw_input("Enter a vote (1 for " + cand1 + ", 2 for " + cand2 + ", 3 for " + cand3 + ", 0 to exit and tabulate votes):\n") #Otherwise, ask for a command/vote
        if num.isdigit() : #Verify that the command is valid
                try :
                        num = int(num)
                        if num == 0 : #If command is exit and tabulate (0), do so.
                                print "##################################################################\n\nAnd the winner(s) is...\n"
                                n = 0
                                winner = 0
                                for i in varray : #Calculate each candidate's votes
                                        n = n+1
                                        if i > winner :
                                                winner = i
                                                winnum = n
                                        if n == 1 :
                                                one = i
                                        elif n == 2 :
                                                two = i
                                        elif n == 3 :
                                                thr = i
                                if winnum == 1 : #Print the winners and their vote percentages
                                        print cand1 + " with " + str(one) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(one)/float(orignum-numvote))*float(100)) + " percent)."
                                elif winnum == 2 :
                                        print cand2 + " with " + str(two) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(two)/float(orignum-numvote))*float(100)) + " percent)."
                                elif winnum == 3 :
                                        print cand3 + " with " + str(thr) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(thr)/float(orignum-numvote))*float(100)) + " percent)."
                                if one == winner and winnum != 1 :
                                        print cand1 + " with " + str(one) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(one)/float(orignum-numvote))*float(100)) + " percent)."
                                if two == winner and winnum != 2 :
                                        print cand2 + " with " + str(two) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(two)/float(orignum-numvote))*float(100)) + " percent)."
                                if thr == winner and winnum != 3 :
                                        print cand3 + " with " + str(thr) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(thr)/float(orignum-numvote))*float(100)) + " percent)."
                                print "\nThe total vote breakdown is as follows:\n" #Print total vote breakdown
                                print cand1 + " had " + str(one) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(one)/float(orignum-numvote))*float(100)) + " percent)."
                                print cand2 + " had " + str(two) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(two)/float(orignum-numvote))*float(100)) + " percent)."
                                print cand3 + " had " + str(thr) + " vote(s) out of " + str(orignum-numvote) + " (" + str((float(thr)/float(orignum-numvote))*float(100)) + " percent)."
                                raw_input()
                                sys.exit()
                        if num > 3 : #Invalid command (only 3 candidates)
                                print "Invalid Number - Please Try Again" #error
                                vote(numvote,cand1,cand2,cand3,varray,orignum) #call vote function
                        varray = tabulate(num,varray) #otherwise, everything is good, tabulate the vote.
                        print "Vote Tabulated Successfully! - " + str(numvote-1) + " votes left!" #print successful
                        numvote = int(numvote)-1 #subtract one from the available votes
                        vote(numvote,cand1,cand2,cand3,varray,orignum) #call vote function
                except ValueError : #invalid number
                        print "Invalid Number - Please Try Again" #error
                        vote(numvote,cand1,cand2,cand3,varray,orignum) #call vote function
        print "Invalid Number - Please Try Again" #error
        vote(numvote,cand1,cand2,cand3,varray,orignum) #call vote function

def tabulate(num,vdarray) : #Tabulate individual Votes Function
        n = 1
        one = 0
        two = 0
        thr = 0
        for i in vdarray : #extract the data from the array
                if n == 4 :
                        break
                elif n == 3 :
                        thr = i
                elif n == 2 :
                        two = i
                elif n == 1 :
                        one = i
                n = n+1
        if num == 1 : #tabulate the new vote
                one = one+1
        elif num == 2 :
                two = two+1
        elif num == 3 :
                thr = thr+1
        vdarray = [int(one),int(two),int(thr)] #rebuild the list/array
        return vdarray #return it

# INITIALIZE PROGRAM FUNCTION
def initvote() :
        cand1 = raw_input("Enter the name of candidate #1:\n") #Get initial data and verify
        if cand1 == "" :
                print "Invalid Input - Please Try Again"
                initvote()
        cand2 = raw_input("Enter the name of candidate #2:\n")
        if cand2 == "" :
                print "Invalid Input - Please Try Again"
                initvote()
        cand3 = raw_input("Enter the name of candidate #3:\n")
        if cand3 == "" :
                print "Invalid Input - Please Try Again"
                initvote()
        cand1 = str(cand1)
        cand2 = str(cand2)
        cand3 = str(cand3)
        varray = [0,0,0] #create initial array
        num = raw_input("Enter the total number of votes allowed:\n") #Get number of votes allowed
        if num.isdigit() : #Is number of votes a number?
                try :
                        num = int(num)
                        if num < 1 : #error catching
                                print "Invalid Number - Please Try Again" #error
                                initvote() #restart
                        vote(num,cand1,cand2,cand3,varray,num) #call vote function
                except ValueError : #Invalid number
                        print "Invalid Number - Please Try Again" #error
                        initvote() #restart
        print "Invalid Number - Please Try Again" #error
        initvote() #restart

initvote() #Start Program
