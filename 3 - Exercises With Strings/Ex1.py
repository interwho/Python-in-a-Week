#Ex1.py
#
#Variables:
#n - user input (full name)
#a - location of the space in the string
#
#Input: FirstName LastName
#Output: LastName, FirstName
#Process: Get data > find space > print output

n=raw_input('Please enter your full name:\n') #get user input
a=n.find(' ') #find space
print n[a+1: ] + ', ' + n[0:a] #print output by location
