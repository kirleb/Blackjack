from card import Card
from random import shuffle
from hand import Hand
from bank import Bank

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
        except (ValueError,TypeError):
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
        elif new_name == '':
            continue
        elif (new_name not in player_names):
            player_names.append(new_name)
        else:
            print('Ensure your name is unique')
    return player_names

def generate_player_dict(player_names,play_deck):
    '''Returns a dictionary with players (including the dealer) and their hands'''
    while True:
        starting_balance = input('Please select a low, mid or high starting balance: ').lower()
        if starting_balance == 'mid':
            starting_balance = 100
            break
        elif starting_balance == 'low':
            starting_balance = 50
            break
        elif starting_balance == 'high':
            starting_balance = 500
            break
        print('Please type low, mid or high')


    player_dict = {name: {'hand':Hand(name,play_deck),'bank':Bank(name,starting_balance)} for name in player_names}
    player_dict['dealer']= {'hand': Hand('dealer',play_deck), 'bank': None}


    return player_dict

def place_bet(players_dict):
    banks = [hand_bank['bank'].balance for hand_bank in players_dict.values() if hand_bank['bank'] != None]
    while True:
        try:
            bet = int(input('Place a bet: £'))
        except (TypeError,ValueError) :
            print('Please enter an integer')
            continue
        if bet > min(banks):
            print('Everyone must have at least the bet amount in their bank')
        elif bet == 0:
            print('Please place a bet')
        elif bet < 0:
            print('Don\'t try tricks bet a positive integer')
        else:
            print(f'You have placed a bet of £{bet}')
            return bet

def take_turn(players_dict,player_name,deck):
    hand = players_dict[player_name]['hand']
    print(hand)
    while True:
        hit_or_stand = input('hit or stand?: ').lower()
        if hit_or_stand == 'stand':
            break
        elif hit_or_stand == 'hit':
            hand.hit(deck)
            print(hand)
            if hand.score > 21:
                hand.score = -21
                input()
                break
            elif hand.score == 21:
                input()
                break

def dealers_turn(players_dict,deck):
    hand = players_dict['dealer']['hand']
    print(hand)
    input()
    scores = [hand_bank['hand'].score for hand_bank in players_dict.values() if hand_bank['bank'] !=None] 
    while True:
        if hand.score > 21:
            hand.score = -21
            return
        elif hand.score == 21 or hand.score > max(scores):
            return
        hand.hit(deck)
        print(hand)
        input()

def tie_breaker(winners):
    rank_value_pairs = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
        'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    tie_break_deck = generate_deck()
    shuffle(tie_break_deck)
    while True:
        draws = {winner: None for winner in winners}
        for winner in winners:
            new_card = tie_break_deck.pop()
            print(f'{winner} drew the {new_card}')
            draws[winner] = rank_value_pairs[new_card.rank]
            input()
        winners = [winner for winner,card in draws.items() if card == max(draws.values())]
        if len(winners) > 1:
            continue
        return winners[0]


    



def main():
    player_names = retrieve_player_names(retrieve_number_of_players()) #get player names and start a deck
    play_deck = []

    play_deck = generate_deck() if len(play_deck) < 30 else play_deck #put cards in the deck (if there are less than 30) and shuffle
    shuffle(play_deck)

    players_dict = generate_player_dict(player_names,play_deck) #generate player dict and bet
    bet = place_bet(players_dict)

    for player in player_names:                          # each player and dealer takes their turn
        take_turn(players_dict,player,play_deck)
    dealers_turn(players_dict,play_deck)

    names_scores = {name: players_dict[name]['hand'].score for name in players_dict.keys()}
    winners = [name for name,score in names_scores.items() if score == max(names_scores.values())] # list of player names with highest scores

    winner = winners[0] if len(winners) == 1 else tie_breaker(winners)
    print(winner)

    



if __name__ == '__main__':
    main()
    
