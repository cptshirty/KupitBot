#coding=windows-1250

from page_scraper import scrape_subpages








if __name__ == "__main__":
    products = []
    url = "https://www.kupi.cz"
    shops_fd = open('shops_of_interest.txt',encoding='windows-1250')
    subpages_fd = open('subpages.txt',encoding='windows-1250')
    keywords_fd = open('keywords.txt',encoding='windows-1250')
    subpages = subpages_fd.readlines()
    shops = shops_fd.readlines()
    keywords = keywords_fd.readlines()
    for x in range(len(shops)):
        shops[x] = shops[x].strip('\n') 
    for x in range(len(keywords)):
        keywords[x] = keywords[x].strip('\n') 
    for x in range(len(subpages)):
        subpages[x] = subpages[x].strip('\n') 
    for subpage in subpages:
       print("scraping subpage: " + subpage)
       products += scrape_subpages(url,"/slevy/" + subpage)
    for product in products:
        for key in keywords:
            if key in product.name:
                product.show_deals(shops)

