from django.views.generic.base import TemplateView

from ..forms import LoginForm


class LoginView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return self.render_to_response(context)
