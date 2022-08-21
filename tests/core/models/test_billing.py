from tests.core.models.test_core_base import CoreTestBase


class BillingModelTest(CoreTestBase):

    def test_billing_str_is_equal_to_name(self):
        user = self.make_user()
        order = self.make_order(
            username=user,
            client=self.make_client(
                username=user
            )
        )
        material = self.make_material(
            username=user
        )
        sale = self.make_sale(
            order=order,
            material=material
        )
        billing = self.make_billing(
            venda=sale
        )
        self.assertEqual(str(billing), str(billing.id))
