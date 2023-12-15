# Food Market

import pickle

from stockitem import *


class FoodMarket:
    show_instrumentation = False

    def __init__(self):
        if FoodMarket.show_instrumentation:
            print("** FoodMarket __init__ called.")
        self.__stock_dictionary = {}

    def save(self, file_name):
        """Saves the Food Market to the pickle file.
        Will raise exception if the save fails."""
        if FoodMarket.show_instrumentation:
            print("** FoodMarket save called.")
        with open(file_name, "wb") as out_file:
            pickle.dump(self, out_file)

    @staticmethod
    def load(file_name):
        """Loads the Food Market from pickle file.
        Will rise exception if the load fails."""
        if FoodMarket.show_instrumentation:
            print("** FoodMarket load called.")
        with open(file_name, "rb") as input_file:
            result = pickle.load(input_file)

        # Now update to the versions of loaded stock items
        for stock_item in result.__stock_dictionary.values():
            stock_item.check_version()
        return result

    def store_new_stock_item(self, store_item):
        """Create a new item in the Food Market.
        The item is indexrd on the stock_ref.
        Will rise exception if the item already exists."""
        if FoodMarket.show_instrumentation:
            print("** FoodMarket store_new_stock_item called.")
        if store_item.stock_ref in self.__stock_dictionary:
            raise Exception("The item already exists.")
        self.__stock_dictionary[store_item.stock_ref] = store_item

    def find_stock_item(self, stock_ref):
        """Gets an item from stock dictionary.
        Returns None if there is no item."""
        if FoodMarket.show_instrumentation:
            print("** FoodMarket find_stock_item called.")
        if stock_ref in self.__stock_dictionary:
            return self.__stock_dictionary[stock_ref]
        else:
            return None

    def __str__(self):
        if FoodMarket.show_instrumentation:
            print("** Food Market __str__ called.")
        stock = map(str, self.__stock_dictionary.values())
        stock_list = "\n".join(stock)
        template = """
Food Market Stock:

{0}
"""
        return template.format(stock_list)
