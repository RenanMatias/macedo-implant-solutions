import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from utils.pagination import make_pagination

from ..models.client import Client


class ClientListViewBase(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Client
    context_object_name = 'clients'
    template_name = 'core/pages/client_list.html'
    ordering = ['nome']

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            request=self.request,
            queryset=ctx.get('clients'),
            per_page=30
        )

        ctx.update(
            {
                'clients': page_obj,
                'pagination_range': pagination_range,
                'page_title': 'Clientes',
                'page_view': 'clients'
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


class ClientExportExcelView(ClientListViewSearch):

    def get(self, request, *args, **kwargs):
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response = HttpResponse(content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename=relatorio_clientes.xls'  # cspell:disable-line

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Clientes')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = [
            'Tipo',
            'Status',
            'Nome',
            'CPF',
            'CNPJ',
            'Endereço',
            'Número',
            'Complemento',
            'Bairro',
            'Município',
            'Cidade',
            'UF',
            'CEP',
            'Telefone',
            'Celular',
            'CRO-UF',
            'CRO',
            'E-mail',
            'Desconto',
            'Data de Aniversário',
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        # cspell:disable
        rows = self.model.objects.all().values_list(
            'tipo',
            'status',
            'nome',
            'cpf',
            'cnpj',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'municipio',
            'cidade',
            'uf',
            'cep',
            'telefone',
            'celular',
            'cro_uf',
            'cro',
            'email',
            'desconto',
            'data_aniversario',
        )
        # cspell:enable

        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response
