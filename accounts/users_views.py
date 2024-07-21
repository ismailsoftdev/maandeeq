from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.db.models import Count
from .user_forms import CustomUserCreationForm, UserChangeForm, GroupForm


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('users:user_list')

    def form_valid(self, form):
        messages.success(self.request, 'User created successfully.')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update User'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        groups_id = self.request.POST.getlist('groups')
        user.groups.set(groups_id)
        user.save()
        messages.success(self.request, 'User updated successfully.')
        return redirect('users:user_list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'User deleted successfully.')
        return super().form_valid(form)

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'


