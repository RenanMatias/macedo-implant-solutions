from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from ..models.client import Client


@method_decorator(
    login_required(
        login_url='login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ClientListView(ListView):
    model = Client
    queryset = Client.objects.all
    template_name = 'core/pages/client_list.html'
    # paginate_by = 50


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'core/pages/client_create.html'
    success_url = reverse_lazy('core:client_list')
