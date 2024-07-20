from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Brand, Product
from .forms import BrandForm, ProductForm

# Brand Views
class BrandListView(ListView):
    model = Brand
    template_name = 'products/products:brand_list.html'
    context_object_name = 'brands'


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'
    context_object_name = 'brand'


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'products/brand_form.html'
    success_url = reverse_lazy('products:brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'products/brand_form.html'
    success_url = reverse_lazy('products:brand_list')


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'products/brand_confirm_delete.html'
    success_url = reverse_lazy('products:brand_list')


# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'products/products:product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Product created successfully.")
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Product update failed.")
        return super().form_invalid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Product deleted successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Product deletion failed.")
        return super().form_invalid(form)
