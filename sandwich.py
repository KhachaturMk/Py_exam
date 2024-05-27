class Sandwich:
    quantity = 1
    price = 0
    ingredients = ''
    name = ''

    def greeting(self):
        print('Welcome to our sandwich shop.\nYour orders:')

class ChickenSandwich(Sandwich):
    price = 10
    ingredients = 'Chicken strips with Teriyaki glaze, served with fresh vegetables and sweet onion sauce.'
    name = 'Chicken Sandwich'

class TunaSandwich(Sandwich):
    price = 13
    ingredients = 'Tuna loaded sub with fresh vegetables and mayo sauce.'
    name = 'Tuna Sandwich'

class SteakAndCheeseSandwich(Sandwich):
    price = 12
    ingredients = 'Portion of steak with american cheese and chipotle sauce.'
    name = 'Steak & Cheese Sandwich'

class VeganSandwich(Sandwich):
    price = 11
    ingredients = 'Spicy vegan patty with fresh vegetables with pickles and crispy onions topping.'
    name = 'Vegan Sandwich'

# orders = [VeganSandwich(),SteakAndCheeseSandwich(), VeganSandwich(),TunaSandwich()]
#
# Sandwich().greeting()
# for order in orders:
#     print(order.name, order.price, 'GEL', order.quantity)
#     print(order.ingredients)
