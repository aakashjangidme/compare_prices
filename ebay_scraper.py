import requests
from bs4 import BeautifulSoup
import re
import json

data = {}
uri = "https://www.ebay.com/itm/NEW-Apple-iPhone-11-128GB-Black-Factory-Unlocked-Fast-Shipping/402317033979"


def ebay_scraper(url):
    ebay_logo = "https://upload.wikimedia.org/wikipedia/commons/4/48/EBay_logo.png"
    ebay_uri = url
    page = requests.get(ebay_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", id="convbinPrice").get_text()
    get_floating_list = re.findall(r"[-+]?\d*\.\d+|\d+", price)
    ebay_price = ""
    ebay_price = ebay_price.join(get_floating_list)
    ebay_title = soup.find("span", id="vi-lkhdr-itmTitl").get_text()

    data['product_info'] = []

    ebay = {
        'name': ebay_title,
        'price': float(ebay_price),
        'url': ebay_uri,
        'logo': ebay_logo,

    }

    data['product_info'].append(ebay)

    return data


print(ebay_scraper(uri))
