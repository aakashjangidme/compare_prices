from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    image = models.CharField(max_length=200)
    slug = models.SlugField(default='', )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # get_absolute_url
        kwargs = {
            # 'pk': self.id,
            'slug': self.slug
        }

        return reverse('prices:product', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, default=1, verbose_name="Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    url = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name
