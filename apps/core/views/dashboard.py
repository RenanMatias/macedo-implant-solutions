from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')

    template_name = 'core/dashboard.html'
