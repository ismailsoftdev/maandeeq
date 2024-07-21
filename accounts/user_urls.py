from django.urls import path
from . import users_views

app_name = 'users'

urlpatterns = [
    path('', users_views.UserListView.as_view(), name='user_list'),
    path('create/', users_views.UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', users_views.UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', users_views.UserDeleteView.as_view(), name='user_delete'),
]
