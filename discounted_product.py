
class DP():
    name = ""
    discount = 0
    og_price = 0
    curr_price = 0
    def __init__(self,name,discount,original_price,price_now):
        self.name = name
        self.discount = discount
        self.og_price = original_price
        self.curr_price = price_now    