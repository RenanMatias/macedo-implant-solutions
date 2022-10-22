import re

from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val=None):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def override_attr(field, attr_name, attr_new_val):
    field.widget.attrs[attr_name] = f'{attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password: str) -> bool:
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            (
                'A senha deve ter pelo menos uma letra maiúscula, uma letra minúscula e um número. '
                'O comprimento deve ser de pelo menos 8 caracteres.'
            ),
            code='Invalid'
        )

    return True
