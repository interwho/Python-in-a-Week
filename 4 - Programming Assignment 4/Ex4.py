####################################
#suit_names - names of suits
#rank_names - names of ranks
#suit - the suit of the card
#rank - the rank of the card
#other - the other card
#self - the first card
#hand - a list of cards
#i - temp count var
#first - first suit
#ret - temp variable
#a - return array variable
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

    def rotate(self,other): #rotate function - change self's suit to other's suit
        self.suit = other.suit
        return self

def rotate_suit(hand): #rotate_suit function - actually change all the suits and return the new hand
    if len(hand) > 0: #if hand exists
        a = [] #init return array
        first = hand[0].suit #first card's suit (for end)
        for i in range(len(hand)-1): #go through each card in hand
            ret = hand[i].rotate(hand[i+1]) #rotate the card's suit with the next one
            a.append(str(ret)) #append it to the return array
        a.append(Card(first,hand[len(hand)-1].rank)) #last card, append with first suit
        return a #return the return array

#Start testing program
hand=[Card(1,9),Card(3,7),Card(2,4),Card(1,7),Card(0,6),Card(0,10),Card(0,9)]
for i in rotate_suit(hand):
    print i
