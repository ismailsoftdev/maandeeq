from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.db.models import Count
from .user_forms import GroupForm



class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Group'
        return context

    def form_valid(self, form):
        group = form.save(commit=False)
        group.save()
        messages.success(self.request, 'Group created successfully.')
        return redirect('groups:group_list')
    
    def form_invalid(self, form):
        error = form.errors
        messages.error(self.request, error)
        return super().form_invalid(form)

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(user_count=Count('user'))


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_form.html'
    success_url = reverse_lazy('groups:group_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Group'
        return context
    
    def form_valid(self, form):
        group = form.save(commit=False)
        group.save()
        messages.success(self.request, 'Group updated successfully.')
        return redirect('groups:group_list')

    def form_invalid(self, form):
        error = form.errors
        messages.error(self.request, error)
        return redirect('groups:group_list')

class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'
    success_url = reverse_lazy('groups:group_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Group deleted successfully.')
        return super().form_valid(form)

