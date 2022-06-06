from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect
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
        if not self.request.POST:
            raise Http404

        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(self.request, authenticated_user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Credenciais inválida.')
            return redirect('login:login')

    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha inválida.')
        return super().form_invalid(form)


class LoginCreate(TemplateView):
    template_name = 'login/create.html'
