class MoneyMachine:
    
    CURRENCY = "$"

    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_recieved = 0

    def report(self):
        # Prints the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        # Returns the total calculated from coins inserted.
        print("Please insert coins.")
        for coin in self.COIN_VALUE:
            self.money_recieved += int(input(f"How many {coin}?: ")) * self.COIN_VALUE[coin]
        return self.money_recieved

    def make_payment(self, cost):
        # Returns True when payment is accepted, or False if insufficient.
        self.process_coins()
        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enoungh money. Money refunded.")
            self.money_recieved = 0
            return False