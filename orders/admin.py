from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'created_at', 'order_total']
    inlines = [OrderItemInline]
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']