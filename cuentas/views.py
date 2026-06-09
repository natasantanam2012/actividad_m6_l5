from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class MiLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('privado')

class MiLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class PaginaPrivadaView(LoginRequiredMixin, TemplateView):
    template_name = 'privado.html'
    login_url = 'login'
