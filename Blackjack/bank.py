class Bank:
    """
    Keeps track of the players money when they start, 
    win or lose a game
    """

    def __init__(self, name, starting_balance):
        
        self.name = name
        self.balance = starting_balance
        self.is_dealer = name =='dealer'
        if not self.is_dealer:
            print(f'{self.name}\'s bank has £{self.balance}')

    @classmethod
    def from_string(cls,name,string):
        '''This constructs a bank object from a string of low, mid or high'''
        #Don't know if lining them up like this is proper
        #but I like the readablity
        string = 500 if string == 'high'\
         else 100 if string == 'mid'\
         else 50 if string == 'low'\
         else 'This shouldn\'t be reachable if validated properly'
        return cls(name,string)
            
    def __str__(self):
        '''String representation of the bank'''
        return f"{self.name} has £{self.balance} in their bank"

    @staticmethod
    def generate_banks(player_names):
        '''Returns a list of banks with low mid or high balance'''
        while True:
            starting_balance = input('Please select a low, mid or '\
                                      'high starting balance: ').lower()
            if starting_balance not in ['low','mid','high']:
                continue
            return [Bank.from_string(player_name,starting_balance) 
                   for player_name in player_names]
    
    @staticmethod
    def update_banks(players_dict,winner,player_names,bet):
        '''
        Returns player_dict and banks with updated banks 
        depending on who won
        '''
        winner_message = 'Dealer wins tough luck' if winner == 'dealer'\
                         else f'{winner} wins Congratulations!!!!'
        print(winner_message)
        #add money to winner minus from losers
        players_dict[winner]['bank']\
        .collect_bets(bet,player_names,players_dict) 
        input()
        banks = [players_dict[player]['bank']
                for player in players_dict.keys()
                if not players_dict[player]['bank'].is_dealer]
        print('\n'.join([str(bank) for bank in banks]))
        return (players_dict,banks)

    def collect_bets(self,bet,remaining_players,players_dict): 
        '''Adds money to winner and subtracts from losers'''                                             
        if not self.is_dealer:
            #adds money from dealer and other players, 
            #added an extra 1 as bet is subracted in next step
            self.balance += (bet*(len(remaining_players)+1))
        for player in remaining_players:
            players_dict[player]['bank'].lose(bet)

    def lose(self,bet):
        '''minuses bet from balance'''
        self.balance -= bet
