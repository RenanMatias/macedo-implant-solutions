from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from utils.pagination import make_pagination

from ..models.client import Client


class ClientListViewBase(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Client
    context_object_name = 'clients'
    template_name = 'core/pages/client_list.html'
    paginate_by = 30
    ordering = ['nome']

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            request=self.request,
            queryset=self.model.objects.all(),
            per_page=self.paginate_by
        )

        ctx.update(
            {
                'clients': page_obj,
                'page_title': 'Clientes',
                'pagination_range': pagination_range,
            }
        )

        return ctx


class ClientListViewSearch(ClientListViewBase):
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        search_term = self.request.GET.get('q', '').strip()

        if not search_term:
            raise Http404()

        qs = qs.filter(
            Q(status__iexact=search_term) | # noqa: W504 E261
            Q(tipo__icontains=search_term) | # noqa: W504 E261
            Q(nome__icontains=search_term) | # noqa: W504 E261
            Q(cpf__icontains=search_term) | # noqa: W504 E261
            Q(cnpj__icontains=search_term),
        )

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '').strip()

        ctx.update({
            'page_title': f'Cliente pesquisa por "{search_term}"',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })

        return ctx


class ClientCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')

    model = Client
    fields = '__all__'
    template_name = 'core/pages/client_create.html'
    success_url = reverse_lazy('core:client_list')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'page_title': 'Novo Cliente'
        })

        return ctx
