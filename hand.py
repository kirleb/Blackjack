from card import rank_value_pairs

class Hand:
    """
    Creates a player or dealer hand, the hand can contain cards and has a score count and aces count.
    Upon construction 2 cards are immediately added.
    """

    def __init__(self,is_dealer):

        self.is_dealer = False
        self.cards = []
        self.score = 0
        self.aces = 0

        self.hit()
        self.hit()

    def __str__(self):
        '''Returns a different string depending on if it is a player or dealer hand'''
        if is_dealer:
            return f'The dealer\'s cards are {" ".join(self.cards)}\nTheir score is {self.score}'
        return f'Your cards are {" ".join(self.cards)}\nYour score is {self.score}'

    def hit(self,card):
        '''Hand recieves a card from the deck, updates the aces count and the hands score '''
        self.cards.append(card)

        if card.ace:
            self.aces += 1

        self.score += rank_value_pairs[card.rank]
        

