from django.views.generic.edit import FormView

from apps.home.forms import HomeForm


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = HomeForm
