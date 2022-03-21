from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
from products.models import Products


class Cart(models.Model):
    sum = models.IntegerField(null=False)
    # product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Products, blank=True)


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
