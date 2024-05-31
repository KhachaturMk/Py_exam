from food_adn_drinks import ChickenSandwich, VeganSandwich, SteakAndCheeseSandwich,TunaSandwich
from food_adn_drinks import EggAndCheeseSandwich, Coca_Cola, Fanta, Borjomi, Likani
def print_form1():
    print('_______________________________________________')
    print("Welcome to Sandwich City! Let's start ordering!")
    print('Press 1 to add product')
    print('Press 2 to remove last product')
    print('Press 3 to view order')
    print('Press 4 to pay')
    print('Press 0 to exit')

def print_form2():
    print('_______________________________________________')
    print('Press 1 to add Chicken Sandwich', ChickenSandwich.price, 'GEL')
    print('Press 2 to add Vegan Sandwich', VeganSandwich.price, 'GEL')
    print('Press 3 to add Steak & Cheese Sandwich', SteakAndCheeseSandwich.price, 'GEL')
    print('Press 4 to add Tuna Sandwich', TunaSandwich.price, 'GEL')
    print('Press 5 to add Egg & Cheese Sandwich', EggAndCheeseSandwich.price, 'GEL')
    print('Press 6 to add Coca-Cola', Coca_Cola.price, 'GEL')
    print('Press 7 to add Fanta', Fanta.price, 'GEL')
    print('Press 8 to add Borjomi', Borjomi.price, 'GEL')
    print('Press 9 to add Likani', Likani.price, 'GEL')
    print('Press 0 to main menu')
    print('_______________________________________________')

def print_form3():
    print('_______________________________________________')
    print('Your order includes:')

def print_form4():
    print('_______________________________________________')