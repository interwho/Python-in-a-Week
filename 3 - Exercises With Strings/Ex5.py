#Ex5.py
#
#Variables:
#sent - user input (sentence)
#others - all other invalid characters
#valid - valid characters table
#i - temporary data transport variable
#
#Input: A Sentence
#Output: The words in the input, reversed, each on it's own line
#Process: Get data > remove invalid characters > check data > split > reverse > print output

sent = raw_input('Enter a sentence to split it by the space:\n') #Get user input
valid = " -BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxzAEIOUYaeiouy0123456789" #valid characters string
others = sent #initialize the other character's variable (to remove everything that isn't valid)
for i in valid:
    others = others.replace(i,'') #remove it
for i in others :
    sent = sent.replace(i,'')
sent = "||" + sent + "||" #check for spaces at the beginning and end of the sentence (half-assed error proofing)
sent = sent.replace("|| ",'')
sent = sent.replace(" ||",'')
sent = sent.replace("||",'') #end space check
sent = sent.split(' ') #split the sentence by spaces
sent = reversed(sent) #reverse the words array/list
for i in sent : #print each word
    print i
