"""This is a touch terminal program for a fast food restaurant.
You can choose and pay for your order without waiting for a cashier.
Spend the saved time on things that are more important to you."""

from print_forms import print_form1,print_form3,print_form4
from pay import BogPayment, TbcPayment
from request import add, menu
from datetime import datetime
import pandas as pd
import random

requests = []
while True:
    un_number = random.randint(10000,99999)
    print_form1()
    inp = input('Press here: -> ')
    if inp == '1':
        print_form4()
        menu(requests)
    if inp == '2':
        add(requests)
    if inp == '3':
        print_form4()
        if len(requests) > 0:
            print(requests[-1].name, 'was removed from order')
            requests.pop()
        else:
            print('Your order list is empty')
    if inp == '4':
        print_form3()
        total = 0
        for i in requests:
            print(i.name, i.price, 'GEL')
            total += i.price
        print('Total price:', total, 'GEL')
    if inp == '5':
        print_form4()
        acc_nummer = input('Enter IBAN account number: -> ')
        if len(requests) > 0 and len(acc_nummer) == 10 and 'GE00TB' in acc_nummer[:6] and acc_nummer[6:].isdigit():
            for request in requests:
                TbcPayment.pay(request)
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      TbcPayment.pay(request), acc_nummer]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price', 'Status', 'IBAN'],
                          mode='a', index=False)
            print(f"Your order {un_number} has been successfully paid\nPlease, take the check")
            exit()
        elif len(requests) > 0 and len(acc_nummer) == 10 and 'GE00BG' in acc_nummer[:6] and acc_nummer[6:].isdigit():
            for request in requests:
                BogPayment.pay(request)
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      BogPayment.pay(request), acc_nummer]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price', 'Status', 'IBAN'],
                          mode='a', index=False)
            print(f"Your order {un_number} has been successfully paid\nPlease, take the check")
            exit()
    if inp == '0':
        for request in requests:
            df = pd.DataFrame(
                [[un_number, datetime.now().replace(microsecond=0), request.name, request.price, 'Not_paid', 'None']])
            df.to_csv('report.csv', header=['Request', 'Year/month/date/time', 'Product', 'Price',
                                            'Status', 'IBAN'], mode='a', index=False)
        print('Exit')
        exit()