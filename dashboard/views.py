from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from orders.models import Order
from customers.models import Customer
from products.models import Product
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if user.groups.filter(name='Admin').exists():
            context['total_products'] = Product.objects.count()
            context['total_customers'] = Customer.objects.count()
            context['total_orders'] = Order.objects.count()
            context['total_users'] = User.objects.count()
            context['latest_orders'] = Order.objects.all().order_by('-created_at')[:5]
            context['latest_customers'] = Customer.objects.all().order_by('-created_at')[:5]
            context['latest_products'] = Product.objects.all().order_by('-created_at')[:5]
        
        elif user.groups.filter(name='Sales').exists():
            context['total_customers'] = Customer.objects.count()
            context['pending_orders'] = Order.objects.filter(status='Pending').count()
            context['completed_orders'] = Order.objects.filter(status='Completed').count()
            context['cancelled_orders'] = Order.objects.filter(status='Cancelled').count()
            context['latest_orders'] = Order.objects.filter(status='Pending', created_by=self.request.user).order_by('-created_at')[:5]
            context['latest_customers'] = Customer.objects.all().order_by('-created_at')[:5]
            context['latest_products'] = Product.objects.all().order_by('-created_at')[:5]
        
        elif user.groups.filter(name='Delivery').exists():
            context['deliverable_orders'] = Order.objects.filter(status='In Progress').count()
            context['completed_orders'] = Order.objects.filter(status='Completed').count()
            context['cancelled_orders'] = Order.objects.filter(status='Cancelled').count()
            context['total_customers'] = Customer.objects.count()
            context['latest_orders'] = Order.objects.filter(deliverable=True).order_by('-created_at')[:5]
            context['latest_customers'] = Customer.objects.all().order_by('-created_at')[:5]
        
        return context
