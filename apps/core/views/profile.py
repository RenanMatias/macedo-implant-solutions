from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages import success
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

from apps.users.forms import UserChangeForm, UserChangePasswordForm
from apps.users.models import User


@method_decorator(
    login_required(
        login_url='login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ProfileView(UpdateView):
    form_class = UserChangeForm
    template_name = 'core/pages/profile_edit.html'
    model = User

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'button_title': 'Atualizar Dados',
            'button_icon': 'bi bi-check2',
            'form_id': 'profile-form',
        })

        return ctx

    def form_valid(self, form):

        form.save()

        success(self.request, 'Dados atualizados com sucesso.')
        return redirect(reverse('core:profile', args=[self.object.pk]))


@method_decorator(
    login_required(
        login_url='login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ProfileChangePasswordView(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'core/pages/profile_change_pass.html'
    # model = User
    success_url = reverse_lazy('core:password')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'button_title': 'Alterar Senha',
            'button_icon': 'bi bi-check2',
        })

        return ctx