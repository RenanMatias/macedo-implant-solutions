from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import LoginForm


class LoginView(FormView):
    template_name = 'login/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('login:create')

    def form_valid(self, form):
        return super().form_valid(form)


class LoginCreate(TemplateView):
    template_name = 'login/create.html'
