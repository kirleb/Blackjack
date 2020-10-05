class Card:
    """Used to create card objects"""

    def __init__(self,suit,rank,is_ace):
        self.suit = suit
        self.rank = rank
        self.is_ace = is_ace
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
