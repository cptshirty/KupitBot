#encoding=windows-1250

class deal():
    vendor = ""
    category = ""
    price = 0
    discount = 0
    def __init__(self,vendor,price,discount,category):
        self.vendor = vendor
        self.price = price
        self.category = category
        self.discount = discount

    def webhook_representation(self):
        return self.vendor,"{:.2f} ".format(self.price) + 'Kč | ' + str(self.discount) + ' % '
    
    def __str__(self):
        details = '| ' + self.vendor +' | '+str(round(self.price,2)) + ' | ' + str(self.discount) + ' % |'
        return details
        
class DP():
    name = ""
    deals = []
    def __init__(self,name,deals):
        self.name = name
        self.deals = deals[:]

    def get_deals(self,shops) -> list:
        deals = []
        for deal in self.deals:
            for shop in shops:
                if shop in deal.vendor:
                    deals.append(deal)
        return deals

    def show_deals(self,shops):
        deals = []
        for deal in self.deals:
            for shop in shops:
                if shop in deal.vendor:
                    deals.append(deal)
        if len(deals) > 0:
            print(self.name)
            print(len(self.name)*'-')
            for deal in deals:
                print(deal)
            print(len(self.name)*'-')