from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class LoginPageView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard:dashboard')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, "Login successful.")
        return super().form_valid(form)

class LogoutPageView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('accounts:login')
