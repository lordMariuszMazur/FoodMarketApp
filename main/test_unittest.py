# unittest for Food Market App

import unittest

from MAZIbox import *
from stockitem import *
from foodmarket import *


class TestMarket(unittest.TestCase):
    def test_StockItem_init(self):
        print("test StockItem.")
        item = StockItem(
            stock_ref="Test",
            price=100,
            expiry_date="01/01/2024",
            country="Australia",
        )
        self.assertEqual(item.stock_ref, "Test")
        self.assertEqual(item.price, 100)
        self.assertEqual(item.expiry_date, "01/01/2024")
        self.assertEqual(item.country, "Australia")

    def test_StockItem_add_stock(self):
        print("test StockItem add_stock.")
        item = StockItem(
            stock_ref="Test",
            price=100,
            expiry_date="01/01/2024",
            country="Australia",
        )
        self.assertEqual(item.stock_level, 0)
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)

    def test_StockItem_sell_stock(self):
        print("test StockItem sell_stock")
        item = StockItem(
            stock_ref="Test",
            price=100,
            expiry_date="01/01/2024",
            country="Australia",
        )
        self.assertEqual(item.stock_level, 0)
        item.add_stock(20)
        self.assertEqual(item.stock_level, 20)
        item.sell_stock(10)
        self.assertEqual(item.stock_level, 10)


if __name__ == "__main__":
    unittest.main()
