####################################
#suit_names - names of suits
#rank_names - names of ranks
#suit - the suit of the card
#rank - the rank of the card
#other - the other card
#self - the first card (aka c1)
#t - the trump card
#trump - the trump card
#c1 - card #1
#c2 - card #2
####################################
class Card(object): #the card class
    '''A playing card - (suit,rank)''' #description
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] #suit array
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King'] #values array

    def __init__ (self,suit=0,rank=1): #initialize the object
        self.suit=suit
        self.rank=rank
    
    def __str__ (self): #format the object as a string when printed
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])

    def who_wins(self,other,trump): #who_wins function - determines winning card
        if self.suit == other.suit: #if the suits are the same
            if self.rank>other.rank: #check the ranks
                return self
            elif self.rank<other.rank:
                return other
        else: #otherwise, return the trump as the winning card
            if Card.suit_names[self.suit]==trump:
                return self
            elif Card.suit_names[other.suit]==trump:
                return other
            else: #no trump, just return c1
                return self

#Start testing program
t="Hearts"
c1=Card(0,3)           
c2=Card(2,7)
print c1.who_wins(c2,t)
