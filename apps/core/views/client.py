from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from utils.pagination import make_pagination_range

from ..models.client import Client


class ClientListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Client
    template_name = 'core/pages/client_list.html'
    paginate_by = 30
    ordering = ['nome']

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_range = ctx['paginator'].page_range
        current_page = ctx['page_obj'].number

        pagination_range = make_pagination_range(
            page_range,
            5,
            current_page
        )

        ctx.update(
            {
                'pagination_range': pagination_range,
            }
        )

        return ctx


class ClientCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')

    model = Client
    fields = '__all__'
    template_name = 'core/pages/client_create.html'
    success_url = reverse_lazy('core:client_list')
