from unittest import TestCase

from utils.cpf_cnpj_validation import cnpj_validate, cpf_validate


class CPF_CNPJ_ValidationTest(TestCase):

    # ************** CPF **************
    def test_cpf_validation_with_correct_cpf_format(self):
        cpf = '321.518.234-31'
        self.assertTrue(cpf_validate(cpf))
        cpf = '32151823431'
        self.assertTrue(cpf_validate(cpf))

    def test_cpf_validation_with_incorrect_cpf_format(self):
        cpf = '321.518.234-3'
        self.assertFalse(cpf_validate(cpf))
        cpf = '3215182343'
        self.assertFalse(cpf_validate(cpf))

    def test_cpf_validation_check_if_cpf_has_not_11_digits(self):
        cpf = '321.518.234-313'
        self.assertFalse(cpf_validate(cpf))

    def test_cpf_validation_check_if_cpf_has_all_digits_are_equal(self):
        cpf = '111.111.111-11'
        self.assertFalse(cpf_validate(cpf))

    def test_cpf_validation_check_first_digit_is_not_correct(self):
        # cpf correct - 321.518.234-31
        cpf = '321.518.234-41'
        self.assertFalse(cpf_validate(cpf))

    def test_cpf_validation_check_second_digit_is_not_correct(self):
        # cpf correct - 321.518.234-31
        cpf = '321.518.234-32'
        self.assertFalse(cpf_validate(cpf))

    # ************** CNPJ **************
    def test_cnpj_validation_with_correct_cnpj_format(self):
        cnpj = '26.262.662/0001-23'
        self.assertTrue(cnpj_validate(cnpj))
        cnpj = '26262662000123'
        self.assertTrue(cnpj_validate(cnpj))

    def test_cnpj_validation_with_incorrect_cnpj_format(self):
        cnpj = '26.262.662/000123'
        self.assertFalse(cnpj_validate(cnpj))
        cnpj = '2626266200012'
        self.assertFalse(cnpj_validate(cnpj))

    def test_cnpj_validation_check_if_cnpj_has_not_14_digits(self):
        cnpj = '12.345.678/9012-345'
        self.assertFalse(cnpj_validate(cnpj))

    def test_cnpj_validation_check_if_cnpj_has_all_digits_are_equal(self):
        cnpj = '11.111.111/1111-11'
        self.assertFalse(cnpj_validate(cnpj))

    def test_cnpj_validation_check_first_digit_is_not_correct(self):
        # cnpj correct - 26.262.662/0001-23
        cnpj = '26.262.662/0001-13'
        self.assertFalse(cnpj_validate(cnpj))

    def test_cnpj_validation_check_second_digit_is_not_correct(self):
        # cnpj correct - 26.262.662/0001-23
        cnpj = '26.262.662/0001-24'
        self.assertFalse(cnpj_validate(cnpj))
