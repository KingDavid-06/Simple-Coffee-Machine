class CoffeeMaker:
    # Models the Machine that makes the coffe.
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        # Prints a report of all resources.
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        # Returns True when order can be made, Dalse if the ingredients are insufficient.
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enought {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        # Deducts the required ingredients from the resources.
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")

        