
class deal():
    vendor = ""
    price = 0
    amount = 0
    discount = 0
    def __init__(self,vendor,price,amount,discount):
        self.vendor = vendor
        self.price = price
        self.amount = amount
        self.discount = discount


class DP():
    name = ""
    deals = []
    def __init__(self,name,deals):
        self.name = name
        self.deals = deals[:]