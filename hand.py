class Hand:
    """
    Creates a player or dealer hand, the hand can contain cards and has a score count and aces count.
    Upon construction 2 cards are immediately added.
    """

    def __init__(self,name):

        self.is_dealer = False
        if name == 'dealer':
            self.is_dealer = True
        self.cards = []
        self.score = 0
        self.aces = 0

        self.hit()
        self.hit()

    def __str__(self):
        '''Returns a different string depending on if it is a player or dealer hand'''
        if is_dealer:
            return f'The dealer\'s cards are {" ".join(self.cards)}\nTheir score is {self.score}'
        return f'{self.name}\'s cards are {" ".join(self.cards)}\n{self.name}\'s score is {self.score}'

    def hit(self,card):
        '''Hand recieves a card from the deck, updates the aces count and the hands score '''
        self.cards.append(card)

        if card.is_ace:
            self.aces += 1

        self.score += rank_value_pairs[card.rank]

    rank_values_pairs = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
    'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        

