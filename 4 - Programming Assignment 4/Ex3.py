####################################
#suit_names - names of suits
#rank_names - names of ranks
#suit - the suit of the card
#rank - the rank of the card
#other - the other card
#self - the first card
#hand - a list of cards
#c - card
#v - rank
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

    def same_value(self,other): #same_value function - returns if both cards are the same rank
        if isinstance(other,Card): #checks that the variable other is a Card object
            if self.rank == other.rank: #are the ranks the same?
                return 1
            else:
                return 0
        else:
            if self.rank == other:
                return 1
            else:
                return 0

def go_fish(hand,other): #returns either the fished card or go fish if it exists in the hand or not
    for i in hand:
        if i.same_value(other) == 1: #are they the same?
            return i
    return 'Go Fish'

#Start testing program
hand=[Card(1,9),Card(3,7),Card(2,4),Card(1,7),Card(0,6),Card(0,10),Card(0,9)]
c=Card(1,6)
v=9
print go_fish(hand,c)
print go_fish(hand,v)
