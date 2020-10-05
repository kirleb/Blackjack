'''
This plays a blackjack game
'''
from random import shuffle

class Card:
    '''
    Class for the formation of cards
    '''
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        
    suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
 
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    rank_value_pairs = {}
 
    for value,rank in enumerate(ranks,2):
    	if value < 11:
    		rank_value_pairs[rank] = value
    		continue
    	if value < 14:
    		rank_value_pairs[rank] = 10
    		continue
    	rank_value_pairs[rank] = 11

print(Card.rank_value_pairs)

a = Card("Clubs","Two")
print(Card.rank_value_pairs,a,sep='\n')
