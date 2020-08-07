from django.urls import path, include

from prices_app.views import HomeView, ProductDetailView
from . import views

app_name = 'prices'
urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('product/<slug>/', ProductDetailView.as_view(), name="product"),
]
