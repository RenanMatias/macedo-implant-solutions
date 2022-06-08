from django.contrib.messages import success
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from apps.home.forms import ContactForm


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = ContactForm

    def form_valid(self, form):
        if not self.request.POST:
            raise Http404

        subject = "Contato do site"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
        }
        message = f"Nome: {body['name']}\nE-mail: {body['email']}\nMensagem: {body['message']}"

        try:
            send_mail(
                subject,
                message,
                'admin@example.com',
                ['admin@example.com'],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        success(self.request,
                'Agradecemos seu contato, em breve entraremos em contato.')

        return redirect('home')
