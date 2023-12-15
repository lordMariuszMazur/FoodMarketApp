# Tests for Food Market App

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


def test_1():
    print("Test 1. StockItem tests.")
    # formatted_now = now.strftime("%d/%m/%Y")
    # 05/12/2023
    x = Vegetables(
        stock_ref="V0001",
        price=100,
        expiry_date="20 / 12 / 2023",
        country="Australia",
        packaging="box",
        size="regular",
    )
    y = Fruits(
        stock_ref="F123987",
        price=50,
        expiry_date="30 / 12 / 2023",
        country="New Zealand",
        packaging="item",
        size="large",
    )

    z = Apples(
        stock_ref="FA0789",
        price=3.99,
        expiry_date="17/12/2023",
        country="China",
        packaging="bag",
        size="1 kg",
        color="Red",
    )
    a = Meat(
        stock_ref="M456",
        price=18.62,
        expiry_date="18/01/2024",
        country="Australia",
        weight="1 kg",
        type_of_meat="Kangaroo",
    )
    b = Drink(
        stock_ref="DD556",
        price=2.14,
        expiry_date="14/01/2024",
        country="New Zealand",
        packaging="bottle",
        size="500 ml",
        alcohol_content="alc 0% ",
    )
    c = Spices(
        stock_ref="SI89",
        price=0.99,
        expiry_date="15/02/2024",
        country="India",
        size="45 g",
        classification="hot",
    )
    d = Seafood(
        stock_ref="SF15001",
        price=8.99,
        expiry_date="20/12/2023",
        country="Australia",
        weight="250 g",
        type_of_seafood="Salmon",
    )
    print(f"Veggie all: \n{x}")
    print(f"Veg {x.expiry_date}, {x.price}")
    print(f"Fruit {y.stock_ref}, {y.size}")
    print(f"Apples {z.packagig}, {z.color}, {z.item_name}")
    print(f"Meat: {a.country}, {a.type_of_meat}")
    print(f"Drink: {b.stock_ref}, {b.alcohol_content}, {b.country}")
    print(f"Spices: {c.price}, {c.classification}")
    print(f"Seafood: {d.expiry_date}, {d.weight}, {d.type_of_seafood}")


def test_2():
    print("Test 2. FoodMarket tests.")
    shop = FoodMarket()
    # shop.save("foodmarket.pickle")
    # loaded_shop = FoodMarket.load("foodmarket.pickle")

    veggie = Vegetables("nj88", 6.32, "12/05/2024", "PNG", "box", "large")

    shop.store_new_stock_item(veggie)
    # print(veggie)

    item = shop.find_stock_item("nj88")
    if item == None:
        print("Item not found.")
    else:
        print(item)

    print(f"Shop:{shop}")


def main_menu():
    menu = """Make a test:
1. StockItem.
2. FoodMarket.
3. Unittest.
4. Exit.
Make a move: """
    while True:
        move = mazi_int_ranged(menu, 1, 4)
        if move == 1:
            test_1()
        elif move == 2:
            test_2()
        elif move == 3:
            if __name__ == "__main__":
                unittest.main()
        elif move == 4:
            print("Exit. Thank you.")
            break


main_menu()
