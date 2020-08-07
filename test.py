import requests
from bs4 import BeautifulSoup
import re
import json

data = {}
data['price'] = []

search_query = 'Apple iPhone 11 128 GB Black'
paytm_logo = "https://www.searchpng.com/wp-content/uploads/2019/02/paytm-Mall-Logo-PNG-768x243.png"
url = "https://paytmmall.com/shop/search?q=%s" % search_query  # url

page = requests.get(url, headers={"User-Agent": "Defined"})
soup = BeautifulSoup(page.content, "html.parser")
paytm_products = soup.find_all('div', class_='_3WhJ')[:1]

for product in paytm_products:
    product_title = product.find(class_="UGUy").get_text()
    product_img = product.find(class_="_3nWP").find("img")['src']
    product_link = "https://paytmmall.com" + str(product.find('a', class_="_8vVO")['href'])
    product_price = product.find(class_="_1kMS").get_text().replace(',', '')

    paytm = {
        'name': product_title,
        'price': float(product_price),
        'url': product_link,
        'logo': paytm_logo,
        'image': product_img

    }

    data['price'].append(paytm)

with open('data2.json', 'w') as f:
    json.dump(data, f)
