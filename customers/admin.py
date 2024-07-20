from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'type', 'email', 'address', 'district', 'subdistrict')
    list_filter = ('type', 'district')
