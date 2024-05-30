from request import add
from print_forms import print_form1,print_form3

requests = []

while True:
    print_form1()
    inp = input('Press here: -> ')
    if inp == '1':
        add(requests)
    if inp == '3':
        print_form3()
        for i in requests:
            print(i.name, i.ingredients, i.price, 'GEL')

    if inp == '0':
        print('Exit')
        exit()