####################################
#suit_names - names of suits
#rank_names - names of ranks
#suit - the suit of the card
#rank - the rank of the card
#other - the other card
#self - the first card
#hand - a list of cards
#clubslist,diamondslist,heartslist,spadeslist - list of each suit's cards in the hand
#ret - temp. return variable
#x - first card (temp)
#y - second card (temp)
#i - temp count var
####################################
class Card(object): #the card class
    '''A playing card - (suit,rank)''' #description
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] #suit array
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King'] #values array

    def __init__ (self,suit=0,rank=1): #initializes the object
        self.suit=suit
        self.rank=rank
    
    def __str__ (self): #format the object as a string when printed
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])

    def highest_in_suit(self, other): #highest_in_suit function - determines highest card out of 2
        if self.rank > other.rank: #self is greater
            return 1
        elif self.rank < other.rank: #other is greater
            return 0
        else: #same card, doesn't matter which is removed
            return 1

def seperate(hand): #seperate the hand into lists of each suit
    clubslist = [] #initialize all the suit arrays
    diamondslist = []
    heartslist = []
    spadeslist = []
    for i in hand: #go through each card and append to it's respective suit
        if i.suit == 0:
            clubslist.append(i)
        elif i.suit == 1:
            diamondslist.append(i)
        elif i.suit == 2:
            heartslist.append(i)
        elif i.suit == 3:
            spadeslist.append(i)
    ret = [clubslist, diamondslist, heartslist, spadeslist] #return a list of the lists
    return ret

def highest_in_each(suit): #highest in each function - takes each suit array and returns the highest value
    try: #catch the last one
        while len(suit) > 0: #while more than 1 element
            x = suit[0] #x is first card
            y = suit[1] #y is second card
            suit.pop(x.highest_in_suit(y)) #remove the smaller card
    except: #onlt largest is left
        return suit[0] #return it

#Start testing program
hand = [Card(1,4), Card(0,7), Card(2,3), Card(3,9), Card(3,10), Card(3,5)]
x = seperate(hand)
clubs = x[0]
diamonds = x[1]
hearts = x[2]
spades = x[3]
print highest_in_each(spades)
print highest_in_each(clubs)
print highest_in_each(diamonds)
print highest_in_each(hearts)
