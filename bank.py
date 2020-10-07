class Bank:
    """Keeps track of the players money when they start, win or lose a game"""

    def __init__(self, name, starting_balance): #make it so they have an option to start with 3 levels of money
        
        self.name = name
        self.balance = starting_balance
        print(f'{self.name}\'s bank has ${self.balance}')

    def __str__(self):
        
        return f"{self.name} has £{self.balance} in their bank"

    def collect_bets(self,bet,remaining_players,players_dict): #remaining_players is a list of remaining players, 
                                                      #players_dict is the dictionary of players
        self.balance += (bet*(len(remaining_players)+1)) # adds money from dealer and other players, added an extra 1 as bet is subracted in next step
        for player in remaining_players:
            players_dict[player]['bank'].lose(bet)


    def lose(self,bet):

        self.balance -= bet

    



