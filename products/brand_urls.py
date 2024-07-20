from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    # Brand URLs
    path('', views.BrandListView.as_view(), name='brand_list'),
    path('<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('new/', views.BrandCreateView.as_view(), name='brand_create'),
    path('<int:pk>/edit/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),
]