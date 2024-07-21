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
    
    def process_order(self, request, queryset):
        for order in queryset:
            order.status = 'In Progress'
            order.deliverable = True
            order.save()
    
    def cancel_order(self, request, queryset):
        for order in queryset:
            order.status = 'Cancelled'
            order.deliverable = False
            order.save()
    
    def complete_order(self, request, queryset):
        for order in queryset:
            order.status = 'Completed'
            order.deliverable = False
            order.save()
    
    actions = ['process_order', 'cancel_order', 'complete_order']