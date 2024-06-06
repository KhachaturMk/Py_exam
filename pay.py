# create main class
class Payment:
    def pay(self):
        pass


# for pay with TBC which is inheritor of main class
class TbcPayment(Payment):
    def pay(self):
        text = 'TBC_pay'
        return text


# for pay with BOG which is inheritor of main class
class BogPayment(Payment):
    def pay(self):
        text = 'BOG_pay'
        return text
