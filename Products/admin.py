from django.contrib import admin

# Register your models here.
from .models import available_products
admin.site.register(available_products)
