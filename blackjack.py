from card import Card
from random import shuffle
'''
This plays a blackjack game
'''
def generate_deck():
    '''returns an unshuffled list of Card objects'''
    suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds') 
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    
    play_deck = []
    for suit in suits:
        for rank in ranks:
            if rank == 'Ace':
                new_card = Card(suit,rank,True)
                play_deck.append(new_card)
                continue
            new_card = Card(suit,rank,False)
            play_deck.append(new_card)
    return play_deck


def main():
    pass

if __name__ == '__main__':
    main()
    play_deck = generate_deck()
    shuffle(play_deck)
    print(play_deck.pop())
