from request import add
from print_forms import print_form1, print_form2

requests = []

while True:
    print_form1()
    inp = input('Select: > ')
    if inp == '1':
        print_form2()
        add(requests)
    if inp == '3':
        print('Your order:')
        for i in requests:
            print(i.name, i.ingredients, i.price, 'GEL')

    if inp == '0':
        print('Exit')
        exit()