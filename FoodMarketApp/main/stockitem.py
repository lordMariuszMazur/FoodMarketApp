# StockItem


class StockItem(object):
    """Stock item in the Food Market."""

    show_instrumentation = False

    min_price = 0.05
    max_price = 500.0

    max_stock_add = 50

    def __init__(self, stock_ref, price, expiry_date, country):
        if StockItem.show_instrumentation:
            print("** StockItem __init__ method.")
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.expiry_date = expiry_date
        self.country = country
        self.StockItem_version = 1

    def check_version(self):  # s 343,399
        """Check the version of this isnstance.
        Upgrades if is necessary to the latest version."""
        if StockItem.show_instrumentation:
            print("** StockItem get check version called.")
        if self.StockItem_version != 1:
            # upgrade to the latest version
            self.StockItem_version = 1

    @property
    def price(self):
        if StockItem.show_instrumentation:
            print("** StockItem get price called.")
        return self.__price

    @property
    def stock_level(self):
        if StockItem.show_instrumentation:
            print("** StockItem get stock level called.")
        return self.__stock_level

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** StockItem get item name called.")
        return "Stock Item"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** StockItem get __str__ called.")
        template = """Stock reference: {0}
Type: {1}
Price: {2}
Stock level: {3}
Expiry date: {4} """
        return template.format(
            self.stock_ref,
            self.item_name,
            self.price,
            self.stock_level,
            self.expiry_date,
        )

    def add_stock(self, count):
        """Adds item to the stock.
        Count gives the number of items can be add.
        Will rise exception when quantity is too big,
        to avoid accidently add to many items."""
        if StockItem.show_instrumentation:
            print("** StockItem add_stock called.")
        if count < 0 or count > StockItem.max_stock_add:
            raise Exception("Incorrect amount. Max 50 items. Please try again.")
        self.__stock_level = self.__stock_level + count

    def sell_stock(self, count):
        """Sells item from the stock.
        Count gives the number of items to sell.
        Will rise exception when quantity is incorrect."""
        if StockItem.show_instrumentation:
            print("** StockItem sell_stock called.")
        if count < 1:
            raise Exception("Incorrect number to sell. Please try again.")
        if count > self.stock_level:
            raise Exception("Not enough item in the stock. Please check stock level.")
        self.__stock_level = self.__stock_level - count

    def set_price(self, new_price):
        """Sets a new price for the item."""
        if StockItem.show_instrumentation:
            print("** StockItem set_price called.")
        if new_price < StockItem.min_price or new_price > StockItem.max_price:
            raise Exception(
                "Price out of range. Min price:",
                StockItem.min_price,
                "max price:",
                StockItem.max_price,
            )
        self.__price = new_price

    @property
    def new_price(self):
        if StockItem.show_instrumentation:
            print("** StockItem get new_price called.")
        return self.__price

    @property
    def stock_level(self):
        if StockItem.show_instrumentation:
            print("** StockItem get stock_level called.")
        return self.__stock_level


class Vegetables(StockItem):
    """Vegetables in the Food Market."""

    def __init__(self, stock_ref, price, expiry_date, country, packaging, size):
        if StockItem.show_instrumentation:
            print("** Vegetables __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.packagig = packaging
        self.size = size
        self.Vegetables_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Vegetables get check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Vegetables get item name called.")
        return "Vegetables"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Vegetables get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Packaging: {1}
Size: {2}"""
        return template.format(stock_details, self.packagig, self.size)


class Fruits(StockItem):
    def __init__(self, stock_ref, price, expiry_date, country, packaging, size):
        if StockItem.show_instrumentation:
            print("** Fruits __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.packagig = packaging
        self.size = size
        self.Fruits_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Fruits check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Fruits item name called.")
        return "Fruits"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Fruits get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Packaging: {1}
Size: {2} """
        return template.format(stock_details, self.packagig, self.size)


class Apples(Fruits):
    def __init__(self, stock_ref, price, expiry_date, country, packaging, size, color):
        if StockItem.show_instrumentation:
            print("** Apples __init__ method.")
        super().__init__(
            stock_ref=stock_ref,
            price=price,
            expiry_date=expiry_date,
            country=country,
            packaging=packaging,
            size=size,
        )
        self.color = color
        self.Apples_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Apples check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Apples item name called.")
        return "Apples"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Apples get __str__ called.")
        fruits_details = super().__str__()
        template = """{0}
Color: {1} """
        return template.format(fruits_details, self.color)


class Meat(StockItem):
    def __init__(self, stock_ref, price, expiry_date, country, weight, type_of_meat):
        if StockItem.show_instrumentation:
            print("** Meat __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.weight = weight
        self.type_of_meat = type_of_meat  # beef,pork,poultry,kangaroo,lamb
        self.Meat_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Meat check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Meat item name called.")
        return "Meat"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Meat get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Weight: {1}
Type of meat: {2} """
        return template.format(stock_details, self.weight, self.type_of_meat)


class Drink(StockItem):
    def __init__(
        self, stock_ref, price, expiry_date, country, packaging, size, alcohol_content
    ):
        if StockItem.show_instrumentation:
            print("** Drink __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.packagig = packaging
        self.size = size
        self.alcohol_content = alcohol_content
        self.Drink_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Drink check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Drink item name called.")
        return "Drink"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Drink get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Packaging: {1} 
Size: {2}
Alcohol content: {3} """
        return template.format(
            stock_details, self.packagig, self.size, self.alcohol_content
        )


class Spices(StockItem):
    def __init__(self, stock_ref, price, expiry_date, country, size, classification):
        if StockItem.show_instrumentation:
            print("** Spices __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.size = size
        self.classification = classification  # hot,mild,aromatic,herbs
        self.Spices_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Spices check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Spices item name called.")
        return "Spices"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Spices get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Size: {1}
Classification: {2} """
        return template.format(stock_details, self.size, self.classification)


class Seafood(StockItem):
    def __init__(self, stock_ref, price, expiry_date, country, weight, type_of_seafood):
        if StockItem.show_instrumentation:
            print("** Seafood __init__ method.")
        super().__init__(
            stock_ref=stock_ref, price=price, expiry_date=expiry_date, country=country
        )
        self.weight = weight
        self.type_of_seafood = type_of_seafood  # cod,salmon,tuna,prawns,mussels
        self.Seafood_version = 1

    def check_version(self):
        if StockItem.show_instrumentation:
            print("** Seafood check version called.")
        super().check_version()

    @property
    def item_name(self):
        if StockItem.show_instrumentation:
            print("** Seafood item name called.")
        return "Seafood"

    def __str__(self):
        if StockItem.show_instrumentation:
            print("** Seafood get __str__ called.")
        stock_details = super().__str__()
        template = """{0}
Weight: {1} 
Type of seafood: {2}"""
        return template.format(stock_details, self.weight, self.type_of_seafood)
