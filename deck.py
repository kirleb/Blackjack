from random import shuffle

class Deck:
    """Creates a deck object that can be shuffled"""

    def __init__(self,cards):
        '''Generates unshuffled instance of a deck'''
        self.deck = cards

    def shuffle(self):
        '''shuffles deck object'''
        random.shuffle(self.deck)




        


