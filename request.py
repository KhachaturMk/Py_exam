from food_adn_drinks import ChickenSandwich, VeganSandwich, SteakAndCheeseSandwich, TunaSandwich
from food_adn_drinks import EggAndCheeseSandwich, Coca_Cola, Fanta, Borjomi, Likani
from print_forms import print_form2

def add(requests):
    while True:
        print_form2()
        item = input('Select product: -> ')
        if item == '1':
            requests.append(ChickenSandwich)
            print('Chicken Sandwich is added in order')
        elif item == '2':
            requests.append(VeganSandwich)
            print('Vegan Sandwich is added in order')
        elif item == '3':
            requests.append(SteakAndCheeseSandwich)
            print('Steak & Cheese Sandwich is added in order')
        elif item == '4':
            requests.append(TunaSandwich)
            print('Tuna Sandwich is added in order')
        elif item == '5':
            requests.append(EggAndCheeseSandwich)
            print('Egg & Cheese Sandwich is added in order')
        elif item == '6':
            requests.append(Coca_Cola)
            print('Coca-Cola is added in order')
        elif item == '7':
            requests.append(Fanta)
            print('Fanta is added in order')
        elif item == '8':
            requests.append(Borjomi)
            print('Borjomi is added in order')
        elif item == '9':
            requests.append(Likani)
            print('Likani is added in order')
        elif item == '0':
            break
        else:
            print('incorrect input')