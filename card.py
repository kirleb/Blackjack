class Card:
    """Used to create card objects"""

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.is_ace = rank == 'Ace'

    def __str__(self):
        '''Returns string representation of a card'''
        return f'{self.rank} of {self.suit}'
