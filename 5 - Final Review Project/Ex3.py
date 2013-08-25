class Card(object): #the card class
    '''A playing card - (suit,rank)''' #description
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] #suit array
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King'] #values array

    def __init__ (self,suit=0,rank=1): #initializes the object
        self.suit=suit
        self.rank=rank
    
    def __str__ (self): #format the object as a string when printed
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])

def suit_count(olist): #Assig. Function
    nlist = [] #init the new return list, and variables to append to it.
    hearts = 0
    diamonds = 0
    spades = 0
    clubs = 0
    for i in olist: #for each in original list, check the suit and increment their respective variable
        if i.suit == 0:
            clubs = clubs + 1
        elif i.suit == 1:
            diamonds = diamonds + 1
        elif i.suit == 2:
            hearts = hearts + 1
        elif i.suit == 3:
            spades = spades + 1
    nlist.append(clubs) #append all the count variables to the new list
    nlist.append(diamonds)
    nlist.append(hearts)
    nlist.append(spades)
    return nlist #return in the format [# of clubs, # of diamonds, # of hearts, # of spades]

#Test Program
hand = [Card(1,4), Card(0,7), Card(2,3), Card(3,9), Card(3,10), Card(3,5)]
for i in suit_count(hand):
    print i
