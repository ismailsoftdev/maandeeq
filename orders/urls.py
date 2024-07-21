from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('',views.OrderListView.as_view(), name='order_list'),
    path('search/', views.CustomerSearchView.as_view(), name='customer_search'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/process/', views.ProcessOrderView.as_view(), name='process_order'),
    path('order/cancel/', views.CancelOrderView.as_view(), name='cancel_order'),
    path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order-item/create/<int:pk>/', views.OrderItemCreateView.as_view(), name='order_item_create'),
    path('order-item/update/<int:pk>/', views.OrderItemUpdateView.as_view(), name='order_item_update'),
    path('order-item/delete/<int:pk>/', views.OrderItemDeleteView.as_view(), name='order_item_delete'),
]
