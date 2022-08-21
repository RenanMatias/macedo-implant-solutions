from django.core.exceptions import ValidationError
from parameterized import parameterized

from tests.core.models.test_core_base import CoreTestBase


class MaterialModelTest(CoreTestBase):

    def test_material_str_is_equal_to_name(self):
        material = self.make_material(
            username=self.make_user()
        )
        self.assertEqual(str(material), material.codigo)

    @parameterized.expand([
        ('codigo', 255),
        ('descricao', 255),
        ('tamanho', 255),
        ('marca', 255),
        ('modelo', 255),
        ('plataforma', 255),
        ('local', 255),
    ])
    def test_material_text_fields_max_length(self, field, max_length):
        user = self.make_user()
        material = self.make_material(
            username=user,
        )
        setattr(material, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            material.full_clean()
