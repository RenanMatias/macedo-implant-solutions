import xlwt
from django.http import HttpResponse


def export_content_excel(response: HttpResponse):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=relatorio_clientes.xlsx'  # cspell:disable-line

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Clientes')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # cspell:disable
    columns = [
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
    ]
    # cspell:enable

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    