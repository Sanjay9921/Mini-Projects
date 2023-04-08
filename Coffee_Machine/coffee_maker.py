class CoffeeMaker:
    """Models the machine that makes the coffee"""
    
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        
    def report(self):
        """Prints a report of all resources"""
        wasser = self.resources["water"]
        milch = self.resources["milk"]
        kaffee = self.resources["coffee"]
        
        print(f"{wasser}ml")
        print(f"{milch}ml")
        print(f"{kaffee}g")
        
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made if resources are sufficient, else False"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")