class Card(object): #the card class
    '''A playing card - (suit,rank)''' #description
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] #suit array
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King'] #values array

    def __init__ (self,suit=0,rank=1): #initializes the object
        self.suit=suit
        self.rank=rank
    
    def __str__ (self): #format the object as a string when printed
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])

def all_reds(olist): #assig. function
    nlist = [] #init the new list (for return)
    for i in olist: #foreach in list of cards, check the suit. If red, append to the new list
        if i.suit == 1: #diamonds
            nlist.append(i)
        elif i.suit == 2: #hearts
            nlist.append(i)
    return nlist #return the new list

#Program test
hand = [Card(1,4), Card(0,7), Card(2,3), Card(3,9), Card(3,10), Card(3,5)]
for i in all_reds(hand):
    print i
