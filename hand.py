class Hand:
    """
    Creates a player or dealer hand, the hand can contain cards and has a score count and aces count.
    Upon construction 2 cards are immediately added.
    """

    def __init__(self,name,deck):

        self.is_dealer = name == 'dealer'
        self.cards = []
        self.score = 0
        self.aces = 0
        self.name = name

        self.hit(deck)
        self.hit(deck)

    def __str__(self):
        '''Returns a different string depending on if it is a player or dealer hand'''
        card_list = [str(card) for card in self.cards]   
        if self.is_dealer:
            return f'The dealer\'s cards are \n'\
                    +',\n'.join(card_list)\
                    +f'\nTheir score is {self.score}'
        return f'{self.name}\'s cards are \n'\
                +',\n'.join(card_list)\
                +f'\n{self.name}\'s score is {self.score}'

    def hit(self,deck):
        '''
        Takes a deck, Hand recieves a card from the deck,
        updates the aces count and the hands score
        '''
        rank_value_pairs = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
                            'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
                            'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        card = deck.pop()
        self.cards.append(card)
        if card.is_ace:
            self.aces += 1
        self.score += rank_value_pairs[card.rank]
        if self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1
           