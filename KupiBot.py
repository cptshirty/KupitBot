#coding=windows-1250
import discord_webhook as dw
import discounted_product as dp
from page_scraper import scrape_subpages
import sys

def print_products(products,subpages,keywords,shops):
    for index,cathegory in enumerate(products):
        print("kategorie: " + subpages[index])
        for product in cathegory:
            for key in keywords:
                if key in product.name:
                    product.show_deals(shops)

def hook_products(API_KEY,products,subpages,keywords,shops,colors):
    webhook = dw.DiscordWebhook(API_KEY,"","KupiBot","https://i.imgur.com/oBPXx0D.png",rate_limit_retry=True)
    for index,cathegory in enumerate(products):
        webhook.set_content( '**' + subpages[index] + '**')
        embeds = []
        for product in cathegory:
            for key in keywords:
                if key in product.name:
                    embed = dw.DiscordEmbed(product.name,"",color=colors[index])
                    deals = product.get_deals(shops)
                    valid_deals = False
                    for deal in deals:
                        if deal.discount != 0:
                            shopname,arrayvalue = deal.webhook_representation()
                            embed.add_embed_field(name=shopname,value=arrayvalue)
                            valid_deals = True
                    if len(deals) > 0 and valid_deals:
                        embeds.append(embed)
        for i in range(0,len(embeds),10):
            if i+10 < len(embeds):
                webhook.embeds = embeds[i:i+10]
            else:
                webhook.embeds = embeds[i:]
            webhook.execute()
            webhook.remove_embeds()


if __name__ == "__main__":
    API_KEY = sys.argv[1]
    url = "https://www.kupi.cz"
    shops_fd = open('shops_of_interest.txt',encoding='windows-1250')
    subpages_fd = open('subpages.txt',encoding='windows-1250')
    keywords_fd = open('keywords.txt',encoding='windows-1250')
    subpages = subpages_fd.readlines()
    products = []
    colors = []
    shops = shops_fd.readlines()
    keywords = keywords_fd.readlines()
    shops = [shop.strip('\n') for shop in shops]
    keywords = [keyword.strip('\n') for keyword in keywords]
    subpages_and_colors = [subpage.strip('\n').split(' ') for subpage in subpages]
    subpages = [duo[0] for duo in subpages_and_colors]
    colors = [duo[1] for duo in subpages_and_colors]
    shops_fd.close()
    subpages_fd.close()
    keywords_fd.close()
    for index,subpage in enumerate(subpages):
       print("scraping subpage: " + subpage)
       products.append(scrape_subpages(url,"/slevy/", subpage))

    print_products(products,subpages,keywords,shops)
    hook_products(API_KEY,products,subpages,keywords,shops,colors)