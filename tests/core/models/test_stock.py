from tests.core.models.test_core_base import CoreTestBase


class StockModelTest(CoreTestBase):

    def test_stock_str_is_equal_to_name(self):
        stock = self.make_stock(
            material=self.make_material(
                username=self.make_user()
            ),
        )
        self.assertEqual(str(stock), stock.material.codigo)
