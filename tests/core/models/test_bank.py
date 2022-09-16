from tests.core.models.test_core_base import CoreTestBase


class BankModelTest(CoreTestBase):

    def test_bank_str_is_equal_to_name(self):
        bank = self.make_bank()
        self.assertEqual(str(bank), str(bank.nome))
