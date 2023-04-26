from django.db import models

# Create your models here.
class property(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postal_code = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    bedrooms = models.IntegerField(default=0)
    sqft = models.DecimalField(max_digits=10, decimal_places=3)
    bathrooms = models.IntegerField(default=0)

    def __str__(self):
        return self.address


