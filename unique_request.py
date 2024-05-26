import random


def unique_request():
    random_number = random.randint(0000, 9999)
    while len(str(random_number)) != 4:
        random_number = random.randint(0000, 9999)
    acc_number = 'Request_' + str(random_number)
    return acc_number