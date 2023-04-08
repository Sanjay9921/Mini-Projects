class MenuItem:
    """Models each menu item"""
    
    def __init__(self, item_name, water, milk, coffee, cost):
        self.name = item_name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the menu with drinks"""
    
    def __init__(self):
        items = ["latte", "espresso", "cappuccino"]
        wasser = [200, 50, 250] #water
        milch = [150, 0, 50] #milk
        kaffee = [24, 18, 24] #coffee
        koste = [2.5, 1.5, 3]
        
        self.menu = []
        
        for i in range(len(items)):
            menu_item = MenuItem(
                item_name = items[i], 
                water = wasser[i], 
                milk = milch[i], 
                coffee = kaffee[i], 
                cost = koste[i])
            
            self.menu.append(menu_item)
            
    def get_items(self):
        """Returns all available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Searches menu for a particular drink. Returns item/None"""
        
        for item in self.menu:
            if item.name == order_name:
                return item
        
        print("Sorry that item is not available!")