from food_adn_drinks import ChickenSandwich, VeganSandwich, SteakAndCheeseSandwich, TunaSandwich
from food_adn_drinks import EggAndCheeseSandwich, Coca_Cola, Fanta, Borjomi, Likani

def add(requests):
    while True:
        item = input('Select item: ')
        if item == '1':
            requests.append(ChickenSandwich)
        elif item == '2':
            requests.append(VeganSandwich)
        elif item == '3':
            requests.append(SteakAndCheeseSandwich)
        elif item == '4':
            requests.append(TunaSandwich)
        elif item == '5':
            requests.append(EggAndCheeseSandwich)
        elif item == '6':
            requests.append(Coca_Cola)
        elif item == '7':
            requests.append(Fanta)
        elif item == '8':
            requests.append(Borjomi)
        elif item == '9':
            requests.append(Likani)
        elif item == '0':
            break
        else:
            print('incorrect input')