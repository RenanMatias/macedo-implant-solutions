
from django.contrib.messages import success
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from apps.home.forms import ContactForm


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email(form)

        success(self.request,
                'Agradecemos seu contato, em breve entraremos em contato.')

        return redirect('/#contact')
