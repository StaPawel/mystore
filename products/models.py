from django.db import models
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    quantity = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})


