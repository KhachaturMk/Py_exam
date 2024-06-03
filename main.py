"""This is a touch terminal program for a fast food restaurant.
You can choose and pay for your order without waiting for a cashier.
Spend the saved time on things that are more important to you."""

from print_forms import print_form1,print_form3,print_form4
from pay import Payment, BogPayment, TbcPayment
from datetime import datetime
from request import add
import pandas as pd
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
    if inp == '4':
        print_form4()
        acc_nummer = input('Enter your account number: ->')
        if len(acc_nummer) == 10 and 'GE' in acc_nummer[:2] and 'TB' in acc_nummer[4:6]:
            for request in requests:
                TbcPayment.pay(request)
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      TbcPayment.pay(request)]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price/GEL', 'Status'],
                          mode='a', index=False)
            print('Your order has been successfully paid')
            exit()
        elif len(acc_nummer) == 10 and 'GE' in acc_nummer[:2] and 'BG' in acc_nummer[4:6]:
            for request in requests:
                BogPayment.pay(request)
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      BogPayment.pay(request)]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price/GEL', 'Status'],
                          mode='a', index=False)
            print('Your order has been successfully paid')
            exit()

    if inp == '0':
        for request in requests:
            df = pd.DataFrame(
                [[un_number, datetime.now().replace(microsecond=0), request.name, request.price, 'Not paid']])
            df.to_csv('report.csv', header=['Request', 'Year/month/date/time', 'Product', 'Price/GEL', 'Status'],
                      mode='a', index=False)
        print('Exit')
        exit()