from django.urls import path
from .views import (
    BrandListView, BrandDetailView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = 'products'

urlpatterns = [
    # Brand URLs
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/new/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/edit/', BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    # Product URLs
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
