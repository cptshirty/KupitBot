
class deal():
    vendor = ""
    price = 0
    discount = 0
    def __init__(self,vendor,price,discount):
        self.vendor = vendor
        self.price = price
        self.discount = discount

    def deal_detail(self):
        details = '| ' + self.vendor +' | '+str(self.price) + ' | ' + str(self.discount) + ' % |'
        print(len(details)*'-')
        print(details)
        print(len(details)*'-')

class DP():
    name = ""
    deals = []
    def __init__(self,name,deals):
        self.name = name
        self.deals = deals[:]

    def show_deals(self,shops):
        deals = []
        for deal in self.deals:
            for shop in shops:
                if shop in deal.vendor:
                    deals.append(deal)
        if len(deals) > 0:
            print(self.name)
            for deal in deals:
                deal.deal_detail()
