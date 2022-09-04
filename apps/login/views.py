from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .forms import LoginForm


class LoginView(FormView):
    """Page to login

    Args:
        FormView (class): A view that displays a login form.

    Raises:
        Http404: If the request is not POST method.
    """
    template_name = 'login/login.html'
    form_class = LoginForm

    def get_success_url(self):
        """get url if form validated

        Returns:
            view: access the system home page.
        """
        return reverse('core:dashboard')

    def form_valid(self, form):
        """Valid the form.

        Args:
            form (class): FormMixin

        Returns:
            Get system home page if form valid or displays a flash message if form not validated.
        """

        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(self.request, authenticated_user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Credenciais inválida.')
            return redirect('login')

    def form_invalid(self, form):
        """If the form is invalid, displays a flash message.

        Args:
            form (class): FormMixin

        Returns:
            form: render the invalid form
        """
        messages.error(self.request, 'Nome de usuário ou senha inválida.')
        return super().form_invalid(form)


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        messages.success(request, 'Logout realizado com sucesso.')
        logout(request)
        return redirect(reverse('login'))
