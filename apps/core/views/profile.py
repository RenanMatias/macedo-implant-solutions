from django.contrib.auth.decorators import login_required
from django.contrib.messages import error, success
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

from apps.users.forms import UserChangeForm
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
    template_name = 'core/profile.html'
    model = User

    def form_valid(self, form):
        success(self.request, 'Dados atualizados com sucesso.')
        form.save()
        return redirect(reverse('core:profile', args=[self.object.pk]))

    def form_invalid(self, form):
        error(self.request, 'Erro ao atualizar dados.')
        return super().form_invalid(form)
