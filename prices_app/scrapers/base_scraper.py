import requests
from bs4 import BeautifulSoup

data = {}


def base_scraper(uri):
    paytm_uri = uri
    page = requests.get(paytm_uri, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    paytm_price = soup.find("span", class_="_1V3w").get_text().replace(',', '')
    paytm_title = soup.find(class_="NZJI").get_text()
    paytm_product_img = soup.find(class_="_3v_O")["src"]

    # print(paytm_product_img)

    data['product_info'] = []

    paytm = {
        'name': paytm_title,
        'price': float(paytm_price),
        'image': paytm_product_img,

    }

    data['product_info'].append(paytm)

    return data

