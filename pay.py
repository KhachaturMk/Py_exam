class Payment:
    def pay(self):
        text = 'Another pay'
        return text

class TbcPayment(Payment):
    def pay(self):
        text = 'TBC pay'
        return text

class BogPayment(Payment):
    def pay(self):
        text = 'BOG pay'
        return text
