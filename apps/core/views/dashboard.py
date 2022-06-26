from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


@method_decorator(
    login_required(
        login_url='login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update(
            {
                'display_nav': 'dashboard'
            }
        )
        return ctx
