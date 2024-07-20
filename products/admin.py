from django.contrib import admin
from .models import Brand, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'quantity']
    list_filter = ['brand']


