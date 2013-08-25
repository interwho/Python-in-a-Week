#Ex4.py
#
#Variables:
#inp - user input (string)
#letters - table of possible letters
#vowels - table of possible vowels
#numbers - table of possible numbers
#others - all other characters
#i - used as a temporary variable to move letters
#j - used as a temporary variable to check letters
#numb - all the numbers from the string
#letr - all the letters from the string
#vowl - all the vowels from the string
#
#Input: string
#Output: All numbers, letters, vowels, and other objects from the input
#Process: Get data > separate data > print output

inp = raw_input('Enter a string to separate it into different character types:\n') #get user input
letters = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz" #letter table
vowels = "AEIOUYaeiouy" #vowel table
numbers = "0123456789" #number table
others = inp #init the others variable
for i in letters: #if the letter in others exists, remove it
    others = others.replace(i,'')
for i in vowels: #if the vowel in others exists, remove it
    others = others.replace(i,'')
for i in numbers: #if the number in others exists, remove it
    others = others.replace(i,'')
##Now get all other sentences
letr = "" #initialize letters output variable
for i in inp: #if letter is valid, add it to the output
    for j in letters :
        if i == j :
            letr = letr + j
vowl = "" #init vowels output
for i in inp: #if vowel is valid, add it to the output
    for j in vowels :
        if i == j :
            vowl = vowl + j
numb = "" #init numbers output
for i in inp: #if number is valid, add it to the output
    for j in numbers :
        if i == j :
            numb = numb + j
print "Numbers: " + numb #print output
print "Consonants: " + letr
print "Vowels: " + vowl
print "Others: " + others
raw_input('Press the return key to exit...') #allow the user to read the data prior to exiting
