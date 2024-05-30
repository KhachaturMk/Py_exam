from request import add
from print_forms import print_form1,print_form3,print_form4
import pandas as pd

requests = []

while True:
    print_form1()
    inp = input('Press here: -> ')
    if inp == '1':
        add(requests)
    if inp == '2':
        if len(requests) > 0:
            print_form4()
            print(requests[-1].name, 'was removed from order')
            requests.pop()
        else:
            print('Your order list is empty')
    if inp == '3':
        print_form3()
        for i in requests:
            print(i.name, i.ingredients, i.price, 'GEL')

    if inp == '0':
        for request in requests:
            df = pd.DataFrame([[request.name, request.price]])
            df.to_csv('report.csv', header=['Product', 'Price(GEL)'], mode='a', index=False)
        print('Exit')
        exit()