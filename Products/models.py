from django.db import models

# Create your models here.
class available_products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField()
    quantity = models.PositiveIntegerField()

