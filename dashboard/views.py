from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from orders.models import Order, OrderItem
from customers.models import Customer
from products.models import Product
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from collections import OrderedDict

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
            context['latest_orders'] = Order.objects.filter(status='Pending').order_by('-created_at')[:5]
            context['latest_customers'] = Customer.objects.all().order_by('-created_at')[:5]
            context['latest_products'] = Product.objects.all().order_by('-created_at')[:5]
            context['sales_chart'] = self.get_sales_data()
        
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
            context['latest_orders'] = Order.objects.filter(deliverable=True, status__in=['In Progress', 'Completed']).order_by('-created_at')[:5]
            context['latest_customers'] = Customer.objects.all().order_by('-created_at')[:5]
        
        return context
    
    def get_sales_data(self):
        # Get the current year
        current_year = datetime.now().year

        # Generate a list of all months in the current year
        months = [datetime(current_year, i, 1).strftime('%B') for i in range(1, 13)]

        # Aggregate sales data by month for the current year
        sales_data = (
            OrderItem.objects.filter(created_at__year=current_year)
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total_sales=Sum('price'))
            .order_by('month')
        )

        # Initialize a dictionary with all months set to 0
        sales_dict = OrderedDict((month, 0) for month in months)

        for data in sales_data:
            month_str = data['month'].strftime('%B')
            if month_str in sales_dict:
                sales_dict[month_str] = float(data['total_sales'])

        labels = list(sales_dict.keys())
        values = list(sales_dict.values())
        
        return {'labels': labels, 'values': values, 'current_year': current_year}
