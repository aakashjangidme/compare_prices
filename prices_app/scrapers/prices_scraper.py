import requests
from bs4 import BeautifulSoup
import re

data = {}


def scraper(ebay_url, paytm_url):
    # ==========ebay========
    ebay_logo = "https://upload.wikimedia.org/wikipedia/commons/4/48/EBay_logo.png"
    ebay_uri = ebay_url
    page = requests.get(ebay_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", id="convbinPrice").get_text()
    get_floating_list = re.findall(r"[-+]?\d*\.\d+|\d+", price)
    ebay_price = ""
    ebay_price = ebay_price.join(get_floating_list)
    ebay_title = soup.find("span", id="vi-lkhdr-itmTitl").get_text()

    # ============paytm mall==========
    paytm_logo = "https://www.searchpng.com/wp-content/uploads/2019/02/paytm-Mall-Logo-PNG-768x243.png"
    paytm_uri = paytm_url
    page = requests.get(paytm_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    paytm_price = soup.find("span", class_="_1V3w").get_text().replace(',', '')
    paytm_title = soup.find(class_="NZJI").get_text()

    paytm_product_img = soup.find(class_="_3v_O")["src"]

    data['product_info'] = []

    ebay = {
        'name': ebay_title,
        'price': float(ebay_price),
        'url': ebay_uri,
        'logo': ebay_logo,
        'image': paytm_product_img

    }
    paytm = {
        'name': paytm_title,
        'price': float(paytm_price),
        'url': paytm_uri,
        'logo': paytm_logo,
        'image': paytm_product_img

    }

    data['product_info'].append(paytm)
    data['product_info'].append(ebay)

    return data
