# import forms, methods and built-in functions that are necessary to start the program
from print_forms import print_form1,print_form3,print_form4
from pay import BogPayment, TbcPayment
from request import add, menu
from datetime import datetime
import pandas as pd
import random

# create a database in which will be processed each order
requests = []

# create a loop for continuous operation of the program during the order
while True:
    # a unique order number is generated here
    un_number = random.randint(10000,99999)
    # print forms are created in print_forms.py file
    print_form1()
    inp = input('Press here: -> ')
    # for view menu
    if inp == '1':
        print_form4()
        # menu function from file request.py
        menu(requests)
    # for add product in order
    if inp == '2':
        # add function from file request.py
        add(requests)
    # for remove last added product
    if inp == '3':
        print_form4()
        # for remove last added product if the database is not empty
        if len(requests) > 0:
            print(requests[-1].name, 'was removed from order')
            requests.pop()
        else:
            print('Your order list is empty')
    # for view the received order
    if inp == '4':
        print_form3()
        total = 0
        # iterate through the database and shows current order details
        for i in requests:
            print(i.name, i.price, 'GEL')
            total += i.price
        print('Total price:', total, 'GEL')
    # for pay
    if inp == '5':
        print_form4()
        acc_nummer = input('Enter IBAN account number: -> ')
        # for pay with TBC bank
        if len(requests) > 0 and len(acc_nummer) == 10 and 'GE00TB' in acc_nummer[:6] and acc_nummer[6:].isdigit():
            for request in requests:
                TbcPayment.pay(request)
                # adds order details to report.csv file
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      TbcPayment.pay(request), acc_nummer]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price', 'Status', 'IBAN'],
                          mode='a', index=False)
            print(f"Your order {un_number} has been successfully paid\nPlease, take the check")
            exit()
        # for pay with BOG bank
        elif len(requests) > 0 and len(acc_nummer) == 10 and 'GE00BG' in acc_nummer[:6] and acc_nummer[6:].isdigit():
            for request in requests:
                BogPayment.pay(request)
                # adds order details to report.csv file
                df = pd.DataFrame(
                    [[un_number, datetime.now().replace(microsecond=0), request.name, request.price,
                      BogPayment.pay(request), acc_nummer]])
                df.to_csv('report.csv',
                          header=['Request', 'Year/month/date/time', 'Product', 'Price', 'Status', 'IBAN'],
                          mode='a', index=False)
            print(f"Your order {un_number} has been successfully paid\nPlease, take the check")
            exit()
    # for exit without pay
    if inp == '0':
        print_form4()
        # adds order details to report.csv file
        for request in requests:
            df = pd.DataFrame(
                [[un_number, datetime.now().replace(microsecond=0), request.name, request.price, 'Not_paid', '---']])
            df.to_csv('report.csv', header=['Request', 'Year/month/date/time', 'Product', 'Price',
                                            'Status', 'IBAN'], mode='a', index=False)
        print('Order is canceled')
        exit()