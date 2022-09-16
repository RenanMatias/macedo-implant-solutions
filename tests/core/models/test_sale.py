from tests.core.models.test_core_base import CoreTestBase


class SaleModelTest(CoreTestBase):

    def test_sale_str_is_equal_to_name(self):
        user = self.make_user()
        order = self.make_order(
            username=user,
            client=self.make_client(
                username=user
            ),
        )
        material = self.make_material(
            username=user
        )

        sale = self.make_sale(
            order=order,
            material=material
        )
        self.assertEqual(str(sale), str(sale.order.id))
