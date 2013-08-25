#Ex2.py
#
#Variables:
#n - user input (full name)
#a - location of the period in the string
#
#Input: Filename.Extension
#Output: .Extension
#Process: Get data > find period > print output

n=raw_input('Please enter a filename:\n') #get user input
a=n.find('.') #find the period (extension)
print n[a+1: ] #print the extension (with period, to show that it's an extension)
