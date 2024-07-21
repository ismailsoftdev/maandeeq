from django.urls import path
from . import group_views

app_name = 'groups'

urlpatterns = [
    path('', group_views.GroupListView.as_view(), name='group_list'),
    path('create/', group_views.GroupCreateView.as_view(), name='group_create'),
    path('update/<int:pk>/', group_views.GroupUpdateView.as_view(), name='group_update'),
    path('delete/<int:pk>/', group_views.GroupDeleteView.as_view(), name='group_delete'),
]