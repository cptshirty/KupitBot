import requests as req
import discounted_product as dp
Categories = []
Shops = []


def identify_product(text):
    print(text)

def find_product(Website :req.Response):
    products = []
    CATCHPHRASE = '<div class=\"group_discounts active\"' 
    lines = Website.text.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        if CATCHPHRASE in line:

            print(len(line))
           # for y in range(i,len(lines)):
           #     if tabline + '<\div>' in lines[y]:
           #         products.append(identify_product(lines[i+1:y]))
           #         i = y
           #         break
    



def main():
    Website =  req.get("https://www.kupi.cz/slevy/hovezi-maso/billa")
    if(Website.status_code == 200):
        find_product(Website)

    else:
        print("website could not have been scraped")










if __name__ == "__main__":
    main()