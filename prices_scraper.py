import requests
from bs4 import BeautifulSoup
import re
import json

data = {}


def scraper():
    # Delete objects in Django

    product_name = "Apple iPhone 11 128GB Black"
    product_image = "https://assetscdn1.paytm.com/images/catalog/product/M/MO/MOBAPPLE-IPHONETELE288739834431CE/1568902254086_4.jpg"
    # ==========ebay========
    ebay_logo = "https://upload.wikimedia.org/wikipedia/commons/4/48/EBay_logo.png"
    ebay_uri = "https://www.ebay.com/itm/NEW-Apple-iPhone-11-128GB-Black-Factory-Unlocked-Fast-Shipping/402317033979"
    page = requests.get(ebay_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", id="convbinPrice").get_text()
    get_floating_list = re.findall(r"[-+]?\d*\.\d+|\d+", price)
    ebay_price = ""
    ebay_price = ebay_price.join(get_floating_list)
    ebay_title = soup.find("span", id="vi-lkhdr-itmTitl").get_text()

    # ============paytm mall==========================
    paytm_logo = "https://www.searchpng.com/wp-content/uploads/2019/02/paytm-Mall-Logo-PNG-768x243.png"
    paytm_uri = "https://paytmmall.com/apple-iphone-11-128-gb-black-CMPLXMOBAPPLE-IPHONETELE288739834431CE-pdp"
    page = requests.get(paytm_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    paytm_price = soup.find("span", class_="_1V3w").get_text().replace(',', '')
    paytm_title = soup.find(class_="NZJI").get_text()

    # print(paytm_product_img)

    data['product_info'] = []

    ebay = {
        'name': ebay_title,
        'price': float(ebay_price),
        'url': ebay_uri,
        'logo': ebay_logo,

    }
    paytm = {
        'name': paytm_title,
        'price': float(paytm_price),
        'url': paytm_uri,
        'logo': paytm_logo,

    }

    data['product_info'].append(paytm)
    data['product_info'].append(ebay)

    # with open('data.json', 'w') as f:
    #     json.dump(data, f)

    return data


# with open('data.json') as json_file:
#     data = json.load(json_file)
#     print(json.dumps(data, indent=2))

scraper()
