#Ex6.py
#
#Variables:
#inp - user input (menu option)
#word - the input that the user wants to manipulate
#pattern - the pattern to manipulate by
#replacement - (option 3) replacement pattern
#
#Input: Menu Option, Word/Pattern/Replacement
#Output: Counts and updated strings
#Process: Menu > Get data > manipulate > print output

import sys #import the exit command
inp = raw_input("Menu:\n1: Count a pattern\n2: Eliminate a pattern\n3: Substitute a pattern\n4: Exit\n") #print menu options
inp = str(inp) #convert the input to a string for comparing
if inp == '1' :
    #count a pattern
    word = raw_input('Enter a word: ') #get input
    pattern = raw_input('Enter a pattern: ')
    print "The pattern " + pattern + " appears " + str(word.count(pattern)) + " time(s) in the string: " + word #print output
elif inp == '2' :
    #eliminate a pattern
    word = raw_input('Enter a word: ') #get input
    pattern = raw_input('Enter a pattern: ')
    print "The new string is: " + word.replace(pattern,'') #print output
elif inp == '3' :
    #substitue a pattern
    word = raw_input('Enter a word: ') #get input
    pattern = raw_input('Enter a pattern: ')
    replacement = raw_input('Enter a replacement pattern: ')
    print "The new string is: " + word.replace(pattern,replacement) #print output
else :
    sys.exit() #invalid menu option, exit.
