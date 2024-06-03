class Payment:
    def pay(self):
        pass

class TbcPayment(Payment):
    def pay(self):
        text = 'TBC_pay'
        return text

class BogPayment(Payment):
    def pay(self):
        text = 'BOG_pay'
        return text
