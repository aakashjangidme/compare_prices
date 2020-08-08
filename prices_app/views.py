from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from prices_app.scrapers.base_scraper import base_scraper
from prices_app.scrapers.prices_scraper import scraper

from .models import Product, ProductDetail
import json


# Change the URLs and Product information will be stored in Models, adn will be fetched on FrontEnd w/ Django Templates.

# Base Url for collecting info
base_urii = "https://paytmmall.com/samsung-galaxy-s10-8-gb-128-gb-blue-CMPLXMOBSAMSUNG-GALADUMM20256975CB4F3-pdp"

# Extract Product info for Base Product w/ Ebay and Paytm Scraper
ebay_urii = "https://www.ebay.com/itm/NEW-Samsung-Galaxy-S10-Plus-SM-G975U-128GB-Prism-Blue-Factory-Unlocked/402210248044"
paytm_urii = "https://paytmmall.com/samsung-galaxy-s10-8-gb-128-gb-blue-CMPLXMOBSAMSUNG-GALADUMM20256975CB4F3-pdp"


# Calling scraper to Scrape data on particular product URLs.
base_data = base_scraper(base_urii)
info_data = scraper(ebay_urii, paytm_urii)

# Create and Get a Django model object for each object with JSON.
for product in info_data['product_info']:

    ProductDetail.objects.get_or_create(
        name=product['name'], price=product['price'], url=product['url'], logo=product['logo'])
    prod = ProductDetail.objects.get(name=product['name'])
    print(prod)
# Many to Many field Relation, a Bug here!!
for product_ in base_data['product_info']:

    pro, created = prod.product.get_or_create(title=product_['name'],
                                              price=product_['price'],
                                              image=product_['image'],)
    print(pro)
    print(created)


# Using ClassBased View Rendering!!

class HomeView(ListView):
    model = Product
    context_object_name = 'product_list'

    template_name = "prices/index.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    template_name = "prices/product.html"
