'''This plays a blackjack game'''

from random import shuffle
from card import Card
from hand import Hand
from bank import Bank

def generate_deck(): #maybe make this a static method in Deck
    '''returns an unshuffled list of Card objects'''
    suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    return [Card(suit,rank) for suit in suits for rank in ranks]

def retrieve_number_of_players():
    '''
    Asks how many players and returns number of
    players as an integer
    '''
    while True:
        print('Please Select a integer between 1-4')
        try:
            number_of_players = int(input('Number of Players?: '))
        except (ValueError,TypeError):
            print('That was not a integer')
            continue
        if 5 > number_of_players > 0:
            return number_of_players
        print('That\'s not between 1-4')

def retrieve_player_names(number_of_players):
    '''
    Takes number of players, asks for players names and returns them in a
    list any name is fine as long as it isn't a duplicate, dealer or empty
    and is at least 1 character long and less than 10. spaces before and after
    will be trimmed
    '''
    player_names = []
    while len(player_names) < number_of_players:
        new_name = input(f'Enter a Name {len(player_names)+1}: ').strip()
        if new_name == 'dealer':
            print('You cannot be the dealer')
        elif not 0 < len(new_name) <10:
            pass
        elif new_name in player_names:
            print('Ensure your name is unique')
        else:
            player_names.append(new_name)
    return player_names

def generate_player_dict(player_names,play_deck,banks):
    '''
    Returns a dictionary with players (including the dealer)
    and their hands
    '''
    player_dict = {name: {'hand':Hand(name,play_deck),
                          'bank':bank}
                          for name,bank in zip(player_names,banks)}
    player_dict['dealer']= {'hand': Hand('dealer',play_deck),
                            'bank': Bank('dealer', 'infinite')}
    return player_dict

def place_bet(players_dict):
    '''
    Prompts players to place their bet, all players must have at
    least that amount of money
    '''
    balances = [players_dict[player]['bank'].balance
               for player in players_dict.keys()
               if not players_dict[player]['bank'].is_dealer]
    while True:
        try:
            bet = int(input('Place a bet: £'))
        except (TypeError,ValueError) :
            print('Please enter an integer')
            continue
        if bet > min(balances):
            print('Everyone must have at least the bet amount in their bank')
        elif bet == 0:
            print('Please place a bet')
        elif bet < 0:
            print('Don\'t try tricks bet a positive integer')
        else:
            print(f'You have placed a bet of £{bet}')
            return bet

def take_turn(players_dict,player_name,deck):
    '''Player takes there turn, asks to hit or stand'''
    hand = players_dict[player_name]['hand']
    print(hand)
    while True:
        hit_or_stand = input('hit or stand?: ').lower()
        if hit_or_stand == 'stand':
            break
        if hit_or_stand == 'hit':
            hand.hit(deck)
            print(hand)
            if hand.score > 21:
                hand.score = -21
                print(f'Sorry {player_name} you\'ve bust')
                input()
                break
            if hand.score == 21:
                input()
                break

def dealers_turn(players_dict,deck):
    '''Does the dealers turn, they hit until they win or bust'''
    hand = players_dict['dealer']['hand']
    print(hand)
    input()
    scores = [players_dict[player]['hand'].score
             for player in players_dict.keys()
             if not players_dict[player]['hand'].is_dealer]
    while True:
        if hand.score > 21:
            hand.score = -21
            print('The dealer has bust good luck')
            input()
            return
        if hand.score == 21 or hand.score > max(scores):
            return
        hand.hit(deck)
        print(hand)
        input()

def tie_breaker(winners):
    '''
    Draws a card for each winner, if the have the highest card
    go into the winners list if they are the last one their name
    is returned
    '''
    rank_value_pairs = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
                       'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
                       'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    tie_break_deck = generate_deck()
    shuffle(tie_break_deck)
    while True:
        draws = {}
        for winner in winners:
            new_card = tie_break_deck.pop()
            print(f'{winner} drew the {new_card}')
            draws[winner] = rank_value_pairs[new_card.rank]
            input()
        winners = [winner for winner,card in draws.items()
                  if card == max(draws.values())]
        if len(winners) > 1:
            continue
        return winners[0]

def remove_losers(players_dict,player_names,banks):
    '''
    Removes people with 0 balances from player_names and banks
    and says the losers are out of money
    '''
    losers = [player_name for player_name in player_names
             if players_dict[player_name]['bank'].balance == 0]
    banks = [bank for bank in banks if bank.balance != 0]
    for loser in losers:
        print(f'{loser} you are out of money. Goodbye')
        player_names.remove(loser)
    return (player_names,banks)

def play_again(banks):
    '''
    True if input is yes, false if no.
    Also false if no banks and says exit message
    '''
    if not banks:  #had if len(banks) == 0 but empty list is falsy
        print('Sorry you are all out of money')
        return False
    while True:
        again = input('Play again? ').lower()
        if not again in ('yes','no'):
            print('Please enter yes or no')
            continue
        return again == 'yes'

def main():
    '''Runs the script for playing the game'''
    #get player names,banks and start a deck
    player_names = retrieve_player_names(retrieve_number_of_players())
    banks = Bank.generate_banks(player_names)
    play_deck = []

    while True:
        #put cards in the deck (if there are less than 30) and shuffle
        play_deck = generate_deck() if len(play_deck) < 30 else play_deck
        shuffle(play_deck)

        #generate player dict and bet
        players_dict = generate_player_dict(player_names,play_deck,banks)
        bet = place_bet(players_dict)

        #each player and dealer takes their turn
        for player in player_names:
            take_turn(players_dict,player,play_deck)
        dealers_turn(players_dict,play_deck)

        #list of player names with highest scores
        names_scores = {name: players_dict[name]['hand'].score
                       for name in players_dict.keys()}
        winners = [name for name,score in names_scores.items()
                  if score == max(names_scores.values())]

        #sets the winner, tie breaks if requires (highest card draw)
        winner = winners[0] if len(winners) == 1 else tie_breaker(winners)

        #don't really like how it looks but want to keep under 79 line length
        players_dict,banks = Bank.update_banks(players_dict,winner,
                                               player_names,bet)

        input()

        #doesn't remove from players_dict that is remade later
        player_names,banks = remove_losers(players_dict,player_names,banks)

        if play_again(banks):
            continue
        print('Thanks for playing my game')
        input()
        return

if __name__ == '__main__':
    main()
