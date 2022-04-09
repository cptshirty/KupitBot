#coding=windows-1250
from typing import List
import requests as req
import discounted_product as dp
from bs4 import BeautifulSoup as soup
import regex
def find_longest(generator):
    strings = []
    for i in generator:
        string = repr(i)
        string = string.replace('\'','')
        string = string.replace(u'\\xa0',u' ')
        strings.append(string)
    strings.sort(reverse=True)
    return strings[0]


def soupsearch(textsoup:soup,category,products):
    ENTRY_CATCHPHRASE = 'group_discounts active'
    NAME_CATCHPHRASE = 'product_link_history'
    TABLE_CATCHPHRASE = 'wide discounts_table' 
    VENDOR_CATCHPHRASE = 'discounts_shop_name'
    PRICE_CATCHPHRASE = 'discount_price_value'
    DISCOUNT_CATCHPHRASE = 'discount_percentage'
    divs = textsoup.find_all('div',{'class':ENTRY_CATCHPHRASE})
    for div in divs:
        stripped_names = div.find('a',{'class':NAME_CATCHPHRASE}).stripped_strings
        product_name = find_longest(stripped_names).lower()
        table = div.find('table',{'class':TABLE_CATCHPHRASE})
        table_entries = table.find_all('tr')
        prod = dp.DP(product_name,[])
        for entry in table_entries:
            shop = ''
            price = '0'
            discount = '0'
            table_shops = entry.find('span')
            table_prices = entry.find('strong')
            table_discounts = entry.find('div',{'class':DISCOUNT_CATCHPHRASE})
            if table_shops != None:
                shop = find_longest(table_shops.stripped_strings).lower()
                split = regex.split("\\\\n + ",shop)
                if len(split) > 1:
                    shop = split[0] + ' ' + split[1]
            if table_prices != None:
                price = find_longest(table_prices.stripped_strings).replace(',','.')
                price = regex.findall("[\\d.]+",price)[0]
            if table_discounts != None:
                discount = find_longest(table_discounts.stripped_strings).replace(',','.')
                discount = regex.findall("[\\d.]+",discount)[0]
            deal = dp.deal(shop,float(price),float(discount),category)
            prod.deals.append(deal) 
        products.append(prod)
    return products

def check_for_more_button(thesoup:soup):
    button = thesoup.find_all('a',{'class':'btn btn_colored big load_discounts'})
    next_page = None
    for but in button:
        if 'Načíst další zboží' in but.text:
            next_page = but.get('href')
            break
    return next_page

def scrape_page(url:str):
    Website = req.get(url)
    text = Website.text
    if(Website.status_code != 200):
        raise ValueError("Website " + url + " could not have been scraped, HTML status code " + str(Website.status_code))
    return text

def scrape_subpages(top_url,second_url,first_subadress):
    products = []
    url = top_url + second_url + first_subadress
    text = scrape_page(url)
    textsoup = soup(text,features="lxml")
    while True:
        subpage = check_for_more_button(textsoup)
        if subpage == None:
            break
        soupsearch(textsoup,first_subadress,products)
        url = top_url + subpage
        textsoup = soup(scrape_page(url),features="lxml")
    return products


if __name__ == "__main__":
    url = "https://www.kupi.cz"
    scrape_subpages(url,"/slevy/","ovoce-a-zelenina")
