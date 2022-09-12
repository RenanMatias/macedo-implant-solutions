from django.urls import resolve, reverse

from apps.core.views.client import ClientExportExcelView
from tests.core.client.test_client_base import ClientTestBase


class ClientListViewExportExcelTest(ClientTestBase):
    
    def test_client_export_excel_view_is_correct(self):
        view = resolve(reverse('core:client_export_excel'))
        self.assertIs(view.func.view_class, ClientExportExcelView)
