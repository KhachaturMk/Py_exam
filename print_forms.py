from food_adn_drinks import ChickenSandwich, VeganSandwich, SteakAndCheeseSandwich
from food_adn_drinks import TunaSandwich, EggAndCheeseSandwich, Coca_Cola, Fanta
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
    print('Press 1 to add', ChickenSandwich.name, ChickenSandwich.price, 'GEL')
    print('Press 2 to add', VeganSandwich.name, VeganSandwich.price, 'GEL')
    print('Press 3 to add', SteakAndCheeseSandwich.name, SteakAndCheeseSandwich.price, 'GEL')
    print('Press 4 to add', TunaSandwich.name, TunaSandwich.price, 'GEL')
    print('Press 5 to add', EggAndCheeseSandwich.name, EggAndCheeseSandwich.price, 'GEL')
    print('Press 6 to add', Coca_Cola.name, Coca_Cola.price, 'GEL')
    print('Press 7 to add', Fanta.name, Fanta.price, 'GEL')
    print('Press 0 to main menu')
    print('_______________________________________________')

def print_form3():
    print('_______________________________________________')
    print('Your order includes:')

def print_form4():
    print('_______________________________________________')