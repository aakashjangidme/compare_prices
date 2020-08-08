from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from prices_app.scrapers.base_scraper import base_scraper
from prices_app.scrapers.prices_scraper import scraper

from .models import Product, ProductDetail
import json
#
# base_urii = "https://paytmmall.com/samsung-galaxy-s10-8-gb-128-gb-blue-CMPLXMOBSAMSUNG-GALADUMM20256975CB4F3-pdp"
# base_data = base_scraper(base_urii)
#
# for product in base_data['product_info']:
#     print(product)
#     Product.objects.create(title=product['name'], price=product['price'], image=product['image'])
#
# ebay_urii = "https://www.ebay.com/itm/NEW-Samsung-Galaxy-S10-Plus-SM-G975U-128GB-Prism-Blue-Factory-Unlocked/402210248044"
#
# paytm_urii = "https://paytmmall.com/samsung-galaxy-s10-8-gb-128-gb-blue-CMPLXMOBSAMSUNG-GALADUMM20256975CB4F3-pdp"
#
# info_data = scraper(ebay_urii, paytm_urii)
#
# # # Create a Django model object for each object in the JSON
# for product in info_data['product_info']:
#     print(product)
#     ProductDetail.objects.create(name=product['name'], price=product['price'], url=product['url'], logo=product['logo'])
#
# with open('data.json') as json_file:
#     json_data = json.load(json_file)


class HomeView(ListView):
    model = Product
    context_object_name = 'product_list'

    template_name = "prices/index.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    template_name = "prices/product.html"
