from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
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

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'button_title': 'Atualizar Dados',
            'button_icon': 'bi bi-check2',
            'form_id': 'profile-form',
        })

        return ctx

    def form_valid(self, form):
        user = form.save(commit=False)

        user.user = self.request.user

        user.save()

        success(self.request, 'Dados atualizados com sucesso.')
        return redirect(reverse('core:profile', args=[self.object.pk]))
