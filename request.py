from food_adn_drinks import ChickenSandwich, VeganSandwich, SteakAndCheeseSandwich, TunaSandwich
from food_adn_drinks import EggAndCheeseSandwich, Coca_Cola, Fanta, Borjomi, Likani
from print_forms import print_form2

def add(requests):
    while True:
        print_form2()
        item = input('Select product: -> ')
        if item == '1':
            requests.append(ChickenSandwich)
            print(ChickenSandwich.name, 'is added in order')
        elif item == '2':
            requests.append(VeganSandwich)
            print(VeganSandwich.name, 'is added in order')
        elif item == '3':
            requests.append(SteakAndCheeseSandwich)
            print(SteakAndCheeseSandwich.name, 'is added in order')
        elif item == '4':
            requests.append(TunaSandwich)
            print(TunaSandwich.name, 'is added in order')
        elif item == '5':
            requests.append(EggAndCheeseSandwich)
            print(EggAndCheeseSandwich.name, 'is added in order')
        elif item == '6':
            requests.append(Coca_Cola)
            print(Coca_Cola.name, 'is added in order')
        elif item == '7':
            requests.append(Fanta)
            print(Fanta.name, 'is added in order')
        elif item == '8':
            requests.append(Borjomi)
            print(Borjomi.name, 'is added in order')
        elif item == '9':
            requests.append(Likani)
            print(Likani.name, 'is added in order')
        elif item == '0':
            break
        else:
            print("Incorrect input, Let's choose a product")