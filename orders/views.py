from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from .forms import CustomerSearchForm, OrderForm, OrderItemForm, OrderItemFormSet
from customers.models import Customer
from products.models import Product

class CustomerSearchView(View):
    def get(self, request):
        form = CustomerSearchForm()
        return render(request, 'orders/customer_search.html', {'form': form})

    def post(self, request):
        query = request.POST.get('query')
        form = CustomerSearchForm(request.POSTa)
        if form.is_valid():
            query = form.cleaned_data['query']
            customers = Customer.objects.filter(name__icontains=query) | Customer.objects.filter(phone__icontains=query)
            if customers.exists():
                return render(request, 'orders/select_customer.html', {'customers': customers})
            else:
                messages.error(request, "No customer found.")
                return redirect('orders:customer_search')
        return render(request, 'orders/customer_search.html', {'form': form})


# class OrderCreateView(View):
#     def get(self, request, customer_id):
#         customer = get_object_or_404(Customer, id=customer_id)
#         order_form = OrderForm()
#         order_item_formset = OrderItemFormSet()
#         return render(request, 'orders/order_form.html', {
#             'order_form': order_form,
#             'order_item_formset': order_item_formset,
#             'customer': customer
#         })

#     def post(self, request, customer_id):
#         customer = get_object_or_404(Customer, id=customer_id)
#         order_form = OrderForm(request.POST)
#         order_item_formset = OrderItemFormSet(request.POST)

#         if order_form.is_valid() and order_item_formset.is_valid():
#             order = order_form.save(commit=False)
#             order.customer = customer
#             order.created_by = request.user
#             order.status = 'pending'
#             order.save()

#             order_items = order_item_formset.save(commit=False)
#             for item in order_items:
#                 item.order = order
#                 item.price = item.quantity * item.product.price
#                 item.save()
            
#             messages.success(request, "Order has been created successfully.")
#             return redirect('orders:order_detail', pk=order.id)

#         return render(request, 'orders/order_form.html', {
#             'order_form': order_form,
#             'order_item_formset': order_item_formset,
#             'customer': customer
#         })

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Order has been created successfully.")
        return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = OrderItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = OrderItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        form.instance.updated_by = self.request.user
        response = super().form_valid(form)
        if items.is_valid():
            items.instance = self.object
            items.save()
            
            messages.success(self.request, "Order has been updated successfully.")
        return response

class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})

    def post(self, request):
        return self.get(request)

class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'orders/order_detail.html', {'order': order})

    def post(self, request, pk):
        return self.get(request, pk)

class OrderDeleteView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'orders/order_delete.html', {'order': order})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        messages.success(request, "Order has been deleted successfully.")
        return redirect('orders:order_list')


class OrderItemCreateView(LoginRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orders/order_item_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.order.id})

    def form_valid(self, form):
        order_id = self.request.POST.get('order_id')
        form.instance.created_by = self.request.user
        form.instance.order = get_object_or_404(Order, id=order_id)
        form.instance.price = form.instance.product.price
        
        messages.success(self.request, "Item has been created successfully.")
        
        return super().form_valid(form)

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orders/order_item_form.html'

    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.order.id})

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        messages.success(self.request, "Item has been updated successfully.")
        return super().form_valid(form)

class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderItem
    template_name = 'orders/order_item_delete.html'

    def get_success_url(self):
        order_item_id = self.kwargs.get('pk')
        order_item = get_object_or_404(OrderItem, id==order_item_id)
        return reverse('orders:order_detail', kwargs={'pk': order_item.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_item = get_object_or_404(OrderItem, id=self.kwargs.get('pk'))
        context['order'] = order_item.order
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Item has been deleted successfully.")
        return super().form_valid(form)