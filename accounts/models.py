from django.db import models
from django.urls import reverse


class User(models.Model):
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id})