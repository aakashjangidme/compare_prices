import requests
from bs4 import BeautifulSoup
import json

data = {}
data['product_info'] = []

# search_query = 'realme-5i-4-gb-64-gb-aqua-blue'
# uri = "https://paytmmall.com/shop/search?q=%s" % search_query  # url

uri = "https://paytmmall.com/realmi-5i-4-gb-64-gb-aqua-blue-CMPLXMOBREALMI-5I-4-DUMM20256C70DAD45-pdp"


def paytm_scraper(url):
    paytm_logo = "https://www.searchpng.com/wp-content/uploads/2019/02/paytm-Mall-Logo-PNG-768x243.png"
    page = requests.get(url, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    paytm_price = soup.find("span", class_="_1V3w").get_text().replace(',', '')
    paytm_title = soup.find(class_="NZJI").get_text()

    paytm = {
        'name': paytm_title,
        'price': float(paytm_price),
        'url': uri,
        'logo': paytm_logo,
    }
    #
    data['product_info'].append(paytm)
    return data


# with open('data2.json', 'w') as f:
#     json.dump(data, f)

print(paytm_scraper(uri))
