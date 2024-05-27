from request import Request
from sandwich import Sandwich, SteakAndCheeseSandwich

my_request = Request

my_request.push(SteakAndCheeseSandwich())
print(my_request)


# while True:
#     task = input('what you want: ')