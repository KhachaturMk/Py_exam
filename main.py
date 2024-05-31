"""This is a touch terminal program for a fast food restaurant.
You can choose and pay for your order without waiting for a cashier.
Spend the saved time on things that are more important to you."""

from request import add
from print_forms import print_form1,print_form3,print_form4
import pandas as pd
from datetime import datetime
import random

requests = []

while True:
    un_number = random.randint(10000,99999)
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
        total = 0
        for i in requests:
            print(i.name, i.ingredients, i.price, 'GEL')
            total += i.price
        print('Total price:', total, 'GEL')
    if inp == '0':
        for request in requests:
            df = pd.DataFrame([[un_number, datetime.now().replace(microsecond=0), request.name, request.price]])
            df.to_csv('report.csv', header=['Request', 'Year/month/date/time', 'Product', 'Price/GEL'], mode='a', index=False)
        print('Exit')
        exit()