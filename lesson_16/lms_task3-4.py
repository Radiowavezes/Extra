from pprint import pprint

class Product:
    '''
    A class to define a product.
    ----------
    Attributes:
    kind : str
        product type
    name : str
        brand name or common name of the prod.
    price : float
        purchase price
    '''
    def __init__(self, kind, name, price):
        self.kind = kind
        self.name = name
        self.price = price


class ProductStore:
    '''
    A class to create a storage of products.
    ----------
    Attributes:
    self.storage : dict
        to store values of product objects
    self.income : float
        to calculate profits
    ----------
    Methods:
    *
    add(product = Product, amount = int):
        to add new type of product or to
        increase the amount of existing one
    *
    set_discount(identifier = str: kind | name, percent = int)
        to set a discount to the specific type of products
        or brand
    *
    sell(product_name = str, amount = int):
        to sell a product if it amount is more than
        what is need to be sold
    *
    get_income():
        to see the calculated profit of sales
    *
    get_all_products():
        to see all position in the storage
    *
    get_product_info(product_name):
        to see how much of product is avaliable
    '''
    def __init__(self):
        self.storage = {}
        self.income = 0

    def add(self, product, amount):
        '''
        Updates the storage dicts with new values.
        If product is already exist, only increases
        it's amount. Prints the storage with pprint
        module after updating.
        '''
        if product.kind not in self.storage:
            self.storage[product.kind] = {
                product.name: {
                    "price": product.price,
                    "sale": round((product.price * 1.3), 2),
                    "total": amount,
                }
            }
            pprint(self.storage[product.kind])
        else:
            for kind, name in self.storage.items():
                if kind == product.kind:
                    if product.name not in name:
                        self.storage[product.kind].update(
                            {
                                product.name: {
                                    "price": product.price,
                                    "sale": round((product.price * 1.3), 2),
                                    "total": amount,
                                }
                            }
                        )
                        pprint(self.storage[product.kind])
                    else:
                        for good, datum in self.storage[product.kind].items():
                            if product.name.lower() == good.lower():
                                datum["total"] = datum.get("total") + amount
                                pprint(self.storage[product.kind])

    def set_discount(self, identifier, percent):
        '''
        Sets a discout to all brands in kind of product
        or to the spesific brand. Prints the message after
        that for make user to be sure everything is done.
        '''
        i = (100 - percent) / 100
        for kind, name in self.storage.items():
            if identifier not in kind:
                for good, datum in name.items():
                    if good.lower() == identifier.lower():
                        datum["sale"] = round(datum.get("sale") * i, 2)
                        print(f'{good} became cheaper for {percent}%' )
            else:
                for good, datum in name.items():
                    datum["sale"] = round(datum.get("sale") * i, 2)
                    print(f'{good} became cheaper for {percent}%' )

    def sell(self, product_name, amount):
        '''
        Decrease the value of total with 'amount 'on the spesific 
        product 'product_name'. If amount is bigger than total,
        raises an error.
        '''
        for name in self.storage.values():
            for good, datum in name.items():
                if product_name.lower() == good.lower():
                    if datum["total"] - amount >= 0:
                        datum["total"] -= amount
                        inc = datum["sale"] - datum["price"]
                        self.income += inc * amount
                        print(f"You've got ${round(inc * amount, 2)}")
                    else:
                        raise BalanceInStockError

    def get_income(self):
        '''
        Returns the self.income value
        '''
        return f"You\'ve earned ${round(self.income, 2)}"

    def get_all_products(self):
        '''
        Prints all the storage dict with module pprint.
        '''
        pprint(self.storage)

    def get_product_info(self, product_name):
        '''
        Returns the amount and the name of
        product_name in case it is present
        in storage anyway.
        '''
        for name in self.storage.values():
            for good, datum in name.items():
                if good.lower() == product_name.lower():
                    return (good, datum["total"])


class BalanceInStockError(BaseException):
    '''
    A class to raise exception if you try to sell more
    of product if it is avaliable.
    '''
    def __str__(self):
        msg = "The balance in stock is less than what needs to be sold"
        with open('logs.txt', 'w', encoding='utf8') as log:
            log.write(msg)
        return msg


s = ProductStore()
onion = Product("VEGETABLES", "Onion", 2.55)
mentos = Product("CANDIES", "Mentos", 1.11)
salmon = Product("FISH", "Salmon", 6.99)
orbit = Product("CANDIES", "Orbit", 1.5)
potatoe = Product("VEGETABLES", "Potatoe", 1.98)
perch = Product("FISH", "Perch", 3.15)
s.add(onion, 59)
s.add(mentos, 75)
s.add(salmon, 65)
s.add(orbit, 42)
s.add(potatoe, 150)
s.add(perch, 69)
s.sell("potatoe", 33)
s.sell("mentos", 25)
s.add(salmon, 10)
print(s.get_income())
s.get_all_products()
s.sell("orbit", 40)
s.get_all_products()
s.add(orbit, 100)
s.set_discount('VEGETABLES', 5)
print(s.get_product_info('Mentos'))
