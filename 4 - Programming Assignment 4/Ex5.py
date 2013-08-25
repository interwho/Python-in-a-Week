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
#na - temp new hand variable
#c - card
#a - indicator variable (temp)
#match - the matched card
#drawn - the drawn card
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

def draw_for_match(hand,drawn): #draw_for_match function
    a = 0 #init detection variable
    na = [] #init new hand
    for i in hand:
        if i.same_value(drawn) == 1: #found the same card!
            a = 1 #indicator to drawn,match return
            match = i #save the matched card
        else:
            na.append(i) #add to the new hand
    hand = na #replace old hand with new hand without matches
    if a == 0: #indicator 0, no matches, add drawn to hand, return none
        hand.append(drawn)
        return None
    else: #indicator 1, match found!
        return [drawn,match]

#Start testing program
hand=[Card(1,9),Card(3,7),Card(2,4),Card(1,7),Card(0,6),Card(0,10),Card(0,9)]
c=Card(1,6)
for i in draw_for_match(hand,c):
    print i
