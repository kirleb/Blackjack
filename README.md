# Blackjack

This project plays a blackjack game.

It makes a bank for each player which is kept for
the whole of the game. When the banks are generated
the player can select a low, medium or high balance.
If the bank balance reaches 0 the player is ejected 
from the game. 
The dealers balance is infinite.

Each round each player and the dealer is given a hand
they can choose to hit(receive a card) or stand(stick
with what they have). If they get 21 or over their 
turn ends automatically.
The dealer will hit until he beats everyones scores or
gets 21.
If more than one player gets the highest card then
they each draw a single card, the highest value card
wins, if more than 1 draws the highest value they
will draw again untill there is a conclusive winner.

The winner then receives the bets from the others
and the dealer, and the others lose those bets.

The players are then presented with the option to play 
again or exit as long as they still have a balance.
If no players have money the game thanks them and
exits.
