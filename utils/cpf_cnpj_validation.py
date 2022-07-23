import re
from itertools import cycle


def cpf_validate(cpf: str) -> bool:
    """Validates the CPF.

    Args:
        cpf (str): CPF to be validated.

    Returns:
        bool: True if the CPF is valid, False otherwise.
    """

    # Check CPF formatting
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) and not re.match(r'\d{11}', cpf):
        return False

    # Get only CPF numbers, ignoring punctuation, if any
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Check if CPF has 11 digits or if all digits are equal
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Check of the first check digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Check of the second check digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def cnpj_valido(cnpj: str) -> bool:
    """Validates the Brazilian CNPJ

    Args:
        cnpj (str): CNPF to be validation

    Returns:
        bool: True if the CNPF is valid, False otherwise.
    """

    # Check CNPJ formatting
    if not re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj) and not re.match(r'\d{14}', cnpj):
        return False

    # Get only CNPJ numbers, ignoring punctuation, if any
    numbers = [int(digit) for digit in cnpj if digit.isdigit()]

    # Check if CNPJ has 14 digits or if all digits are equal
    if len(numbers) != 14 or len(set(numbers)) == 1:
        return False

    # Check
    cnpj_r = ''.join(re.findall(r'\d+', cnpj))[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True
