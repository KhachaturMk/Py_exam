# create main class
class FoodAndDrinks:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients


# menu objects are created based on the FoodAndDrinks class
# each object has name, price and ingredients
ChickenSandwich = FoodAndDrinks('Chicken Sandwich', 10,
                                '(Chicken strips with Teriyaki glaze with onion sauce)')
VeganSandwich = FoodAndDrinks('Vegan Sandwich', 11,
                              '(Spicy vegan patty with fresh vegetables with pickles)')
SteakAndCheeseSandwich = FoodAndDrinks('Steak Sandwich', 12,
                                       '(Steak with american cheese and chipotle sauce)')
TunaSandwich = FoodAndDrinks('Tuna Sandwich', 13,
                             '(Tuna loaded sub with fresh vegetables and mayo sauce)')
EggAndCheeseSandwich = FoodAndDrinks('Egg&Cheese Sandwich', 11,
                                     '(Poached egga and cheese, veggies with mayo sauce)')
Coca_Cola = FoodAndDrinks('Coca Cola', 2, '(Carbonated soft drink)')
Fanta = FoodAndDrinks('Fanta', 2, '(Carbonated soft drink)')