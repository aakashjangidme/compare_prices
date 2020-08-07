from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Product
import json
import requests
from bs4 import BeautifulSoup
from prices_scraper import scraper

# data = scraper()  # use this to scrape price
# print(data['product_info'])

with open('data.json') as json_file:
    json_data = json.load(json_file)


# with open('data2.json') as json_file:
#     json_data2 = json.load(json_file)


class HomeView(ListView):
    model = Product
    context_object_name = 'product_list'

    template_name = "prices/index.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    template_name = "prices/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_info_list"] = json_data['product_info']
        return context
