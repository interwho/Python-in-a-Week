#Ex3.py
#
#Variables:
#inp - user input (full name)
#caps - the table of all possible capitals
#count - the number of capital letters in the string
#
#Input: A String
#Output: # of Capital Letters
#Process: Get data > count capitals > print output

inp = raw_input('Enter a string to count the number of capital letters:\n') #get user input
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #table of caps
count = 0 #initialize the count
for i in caps: #for each letter in caps
    count = count + inp.count(i) #add the number of times that letter appears to count
print count #print the result
