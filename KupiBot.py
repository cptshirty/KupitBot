#coding=windows-1250
import discounted_product as dp
from page_scraper import scrape_subpages








if __name__ == "__main__":
    url = "https://www.kupi.cz"
    shops_fd = open('shops_of_interest.txt',encoding='windows-1250')
    subpages_fd = open('subpages.txt',encoding='windows-1250')
    keywords_fd = open('keywords.txt',encoding='windows-1250')
    subpages = subpages_fd.readlines()
    products = []
    shops = shops_fd.readlines()
    keywords = keywords_fd.readlines()
    for x in range(len(shops)):
        shops[x] = shops[x].strip('\n') 
    for x in range(len(keywords)):
        keywords[x] = keywords[x].strip('\n') 
    for x in range(len(subpages)):
        subpages[x] = subpages[x].strip('\n') 
    for index,subpage in enumerate(subpages):
       print("scraping subpage: " + subpage)
       products.append(scrape_subpages(url,"/slevy/", subpage))
    for index,cathegory in enumerate(products):
        print("kategorie: " + subpages[index])
        for product in cathegory:
            for key in keywords:
                if key in product.name:
                    product.show_deals(shops)

