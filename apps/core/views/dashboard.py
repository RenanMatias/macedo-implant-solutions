from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

# @login_required(login_url='login', redirect_field_name='next')


@method_decorator(
    login_required(
        login_url='login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'
