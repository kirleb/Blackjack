from card import Card
from random import shuffle
from hand import Hand
'''
This plays a blackjack game
'''
def generate_deck(): #maybe make this a static method in Deck
    '''returns an unshuffled list of Card objects'''
    suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds') 
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    
    play_deck = []
    for suit in suits:
        for rank in ranks:
            is_ace = True if rank == 'Ace' else False
            new_card = Card(suit,rank,is_ace)
            play_deck.append(new_card)
    return play_deck

def retrieve_number_of_players():
    '''Asks how many players and returns number of players as an integer'''
    
    while True:
        print('Please Select a integer between 1-4')
        try:
            number_of_players = int(input('Number of Players?: '))
            if number_of_players > 0 and number_of_players < 5:
                return number_of_players
            print('That\'s not between 1-4')
        except ValueError:
            print('That was not a integer')

def retrieve_player_names(number_of_players):
    '''
    Takes number of players, asks for players names and returns them in a list
    any name is fine as long as it isn't a duplicate, dealer or empty
    '''
    player_names = []
    while len(player_names) < number_of_players:
        new_name = input(f'Enter a Name{len(player_names)+1}: ')
        if new_name == 'dealer':
            print('You cannot be the dealer')
        elif (new_name not in player_names):
            player_names.append(new_name)
        else:
            print('Ensure your name is unique')
    return player_names

def generate_hands(player_names,play_deck):
    names_hands = {name: Hand(name,play_deck) for name in player_names}
    return names_hands





def main():
    pass

if __name__ == '__main__':
    main()
    player_names = retrieve_player_names(retrieve_number_of_players())
    play_deck = generate_deck()
    shuffle(play_deck)
    for name,hand in generate_hands(player_names,play_deck).items():
        print(hand)
