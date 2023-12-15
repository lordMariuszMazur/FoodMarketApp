# FoodMarketShell

from stockitem import *
from foodmarket import FoodMarket
from MAZIbox import *


class FoodMarketShell:
    def __init__(self, file_name):
        """Manages the Food Market data.
        Displays a message if the load file failes
        and creates a new data file.
        """
        FoodMarketShell.__file_name = file_name
        try:
            self.__shop = FoodMarket.load(file_name)
        except:
            print("Loading data failed. Create an empty data file.")
            self.__shop = FoodMarket()

    def create_new_stock_item(self):
        """Creates a new item in the stock.
        Gets the details of the item, creates it
        and at the end stores it."""

        item_stock_ref = mazi_text("Enter the stock reference: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item != None:
            print(f"The item already exists.\n{item}")

        menu = """
Create a new item:

1. Vegetables.
2. Friuts.
3. Meat.
4. Drink.
5. Spices.
6. Seafood.
7. Back to main menu.

What would you like to do: """
        while True:
            choice = mazi_int_ranged(prompt=menu, min_value=1, max_value=7)

            if choice == 1:
                print("Create a new Vegetables.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                packaging = mazi_text("Enter packaging: ")
                size = mazi_text("Enter size: ")
                stock_item = Vegetables(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    packaging=packaging,
                    size=size,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 2:
                print("Create a new Friuts.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                packaging = mazi_text("Enter packaging: ")
                size = mazi_text("Enter size: ")
                stock_item = Fruits(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    packaging=packaging,
                    size=size,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 3:
                print("Create a new Meat.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                weight = mazi_text("Enter weight: ")
                type_of_meat = mazi_text(
                    "Enter type of meat(beef,pork,poultry,kangaroo,lamb): "
                )
                stock_item = Meat(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    weight=weight,
                    type_of_meat=type_of_meat,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 4:
                print("Create a new Drink.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                packaging = mazi_text("Enter packaging: ")
                size = mazi_text("Enter size: ")
                alcohol_content = mazi_text("Enter alcohol content: ")
                stock_item = Drink(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    packaging=packaging,
                    size=size,
                    alcohol_content=alcohol_content,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 5:
                print("Create a new Spices.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                size = mazi_text("Enter size: ")
                classification = mazi_text(
                    "Enter classification(hot,mild,aromatic,herbs): "
                )
                stock_item = Spices(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    size=size,
                    classification=classification,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 6:
                print("Create a new Seafood.")
                stock_ref = mazi_text("Enter stock reference: ")
                price = mazi_float_ranged(
                    prompt="Enter price: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                expiry_date = mazi_text("Enter expiry date(dd/mm/rrrr): ")
                country = mazi_text("Enter country the item comes from: ")
                weight = mazi_text("Enter weight: ")
                type_of_seafood = mazi_text(
                    "Enter type of seafood(cod,salmon,tuna,prawns,mussels): "
                )
                stock_item = Seafood(
                    stock_ref=stock_ref,
                    price=price,
                    expiry_date=expiry_date,
                    country=country,
                    weight=weight,
                    type_of_seafood=type_of_seafood,
                )
                try:
                    self.__shop.store_new_stock_item(stock_item)
                    print("Item succesfuly stored.")
                except Exception as e:
                    print("Unlucky. Item not stored.", e)
            elif choice == 7:
                print("Back to main menu.")
                break

    def add_stock(self):
        """Adds item to the existing stock.
        First searches for the item and then gets
        the number of items to add."""
        print("Add stock.")
        item_stock_ref = mazi_text("Enter the stock reference: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print("Item not found. Please check the stock reference.")
        print(item)

        number_to_add = mazi_int_ranged(
            "Enter number of items to add(0 to cancel): ", 0, StockItem.max_stock_add
        )
        if number_to_add == 0:
            print("No items added.")
            return
        else:
            item.add_stock(number_to_add)
            print(item)

    def sell_stock(self):
        """Sells stock. Searches for the item then reads the number
        of items that being sold.
        Will not allow to sell more items than are avalible in stock."""

        item_stock_ref = mazi_text("Enter the stock references: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print("Item not found. Please check the stock reference.")
            return

        if item.stock_level == 0:
            print("Stock is empty.")

        print("Selling", item)

        number_sold = mazi_int_ranged(
            "How many sold(0 to cancel): ", 0, item.stock_level
        )

        if number_sold == 0:
            print("No items selled.")
            return

        item.sell_stock(number_sold)
        print("Items succesfuly sold. Well done.")

    def do_report(self):
        """Prints the stock report."""
        print(
            "Stock report: ",
        )
        if self.__shop == None:
            print("Stock empty.")
        else:
            print(self.__shop)

    def edit_item(self):
        """Edits item in the stock.
        Delete item option avaliable."""

        item_stock_ref = mazi_text("Enter the stock reference: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print("Item not found. Please check the stock reference.")
        else:
            print(f"Edit item.\n{item}")
            try:
                new_stock_ref = mazi_text("Enter new stock reference or * to skip: ")
                if new_stock_ref != "*":
                    item.stock_ref = new_stock_ref
                new_price = mazi_float_ranged(
                    prompt="Enter new price or 500.0 to skip: ",
                    min_value=StockItem.min_price,
                    max_value=StockItem.max_price,
                )
                if new_price != 500.0:
                    item.set_price(new_price)
                new_expiry_date = mazi_text(
                    "Enter new expiry date(dd/mm/rrrr) or * to skip: "
                )
                if new_expiry_date != "*":
                    item.expiry_date = new_expiry_date
                new_country = mazi_text("Enter new country or * to skip: ")
                if new_country != "*":
                    item.country = new_country
                new_item_name = mazi_text("Enter new type or * to skip: ")
                if new_item_name != "*":
                    if (
                        new_item_name == "Vegetables"
                        or "Fruits"
                        or "Meat"
                        or "Drink"
                        or "Spices"
                        or "Seafood"
                    ):
                        item.item_name = new_item_name
                    else:
                        print("Incorrect type.")
                # new_stock_level = mazi_int("Enter new stock level or * to skip: ")
                # if new_stock_level != "*" or new_stock_level < 0:
                # item.stock_level = new_stock_level
                new_packaging = mazi_text("Enter new packagig or * to skip: ")
                if new_packaging != "*" or new_packaging == None:
                    item.packagig = new_packaging
                new_size = mazi_text("Enter new size or * to skip: ")
                if new_size != "*" or None:
                    item.size = new_size
                new_color = mazi_text("Enter new color or * to skip: ")
                if new_color != False:
                    if new_color != "*":
                        item.color = new_color
                new_weight = mazi_text("Enter new weight or * to skip: ")
                if new_weight != "*" or None:
                    item.weight = new_weight
                new_type_of_meat = mazi_text(
                    "Enter new type of meat(beef,pork,poultry,kangaroo,lamb) or * to skip: "
                )
                if new_type_of_meat != "*" or None:
                    item.type_of_meat = new_type_of_meat
                new_alcohol_content = mazi_text(
                    "Enter new alcohol content or * to skip: "
                )
                if new_alcohol_content != "*" or None:
                    item.alcohol_content = new_alcohol_content
                new_classification = mazi_text(
                    "Enter new classification(hot,mild,aromatic,herbs) or * to skip: "
                )
                if new_size != "*" or None:
                    item.classification = new_classification
                new_type_of_seafood = mazi_text(
                    "Enter new type of seafood(cod,salmon,tuna,prawns,mussels) or * to skip: "
                )
                if new_type_of_seafood != "*" or None:
                    item.type_of_seafood = new_type_of_seafood
            except Exception as e:
                print("Edit failed: ", e)

    def main_menu(self):
        market_menu = """Food Market

1. Create a new stock item.
2. Add item to stock.
3. Sell item.
4. Stock report.
5. Edit item in the stock.
6. Exit.

Enter your command: """

        while True:
            command = mazi_int_ranged(prompt=market_menu, min_value=1, max_value=6)

            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
                self.edit_item()
            elif command == 6:
                self.__shop.save(FoodMarketShell.__file_name)
                print("Thank you. Have a nice day.")
                break


# ui = FoodMarketShell("foodmarket1.pickle")
# ui.main_menu()
