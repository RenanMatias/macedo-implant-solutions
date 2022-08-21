from django.core.exceptions import ValidationError
from parameterized import parameterized

from tests.core.models.test_core_base import CoreTestBase


class OrderModelTest(CoreTestBase):

    def test_order_str_is_equal_to_name(self):
        user = self.make_user()
        order = self.make_order(
            username=user,
            client=self.make_client(username=user),
        )
        self.assertEqual(str(order), str(order.id))

    @parameterized.expand([
        ('dentista', 255),
        ('instituicao', 255),
    ])
    def test_order_text_fields_max_length(self, field, max_length):
        user = self.make_user()
        order = self.make_order(
            username=user,
            client=self.make_client(username=user)
        )
        setattr(order, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            order.full_clean()
