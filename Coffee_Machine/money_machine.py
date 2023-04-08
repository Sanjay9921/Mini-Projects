class MoneyMachine:
    
    #Global Var
    CURRENCY = "$"
    
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }
    
    #No Block level indentation in Python!
    def __init__(self):
        self.profit = 0.0
        self.money_received = 0.0
    
    def report(self):
        """Prints the report => current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
        
    def process_coins(self):
        """Returns total calculated from coins inserted"""
        
        print("Please insert coins...")
        
        for coin in self.COIN_VALUES:
            user_coin = int(input(f"How many {coin}?: "))
            self.money_received += user_coin * self.COIN_VALUES[coin]
        
        return self.money_received
    
    def make_payment(self, cost):
        """Returns True if payment is accepted, else False"""
        
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that is not enough money! Money is refunded...")
            self.money_received = 0
            return False