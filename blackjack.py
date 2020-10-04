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
        