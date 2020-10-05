class Bank:
    """Keeps track of the players money when they start, win or lose a game"""

    def __init__(self, starting_balance): #make it so they have an option to start with 3 levels of money
        
        self.balance = starting_balance
        print(f'Bank made with ${self.balance}')

    def __str__(self):
        
        return f"You have ${self.balance} in your bank"

    def win(self,bet):
        
        self.balance += bet

    def lose(self,bet):

        self.balance -= bet

    



