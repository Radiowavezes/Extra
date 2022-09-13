from pprint import pprint


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.storage = {}
        self.income = 0

    def add(self, Product, amount):
        if Product.type not in self.storage:
            self.storage[Product.type] = {
                Product.name: {
                    "price": Product.price,
                    "sale": round((Product.price * 1.3), 2),
                    "total": amount,
                }
            }
        else:
            for type, name in self.storage.items():
                if type == Product.type:
                    if Product.name not in name:
                        self.storage[Product.type].update(
                            {
                                Product.name: {
                                    "price": Product.price,
                                    "sale": round((Product.price * 1.3), 2),
                                    "total": amount,
                                }
                            }
                        )
                    else:
                        for good, datum in self.storage[Product.type].items():
                            if Product.name == good:
                                datum["total"] = datum.get("total") + amount

    def set_discount(self, identifier, percent):
        i = (100 - percent) / 100
        for type, name in self.storage.items():
            if identifier not in type:
                for good, datum in name.items():
                    if good == identifier:
                        datum["sale"] = round(datum.get("sale") * i, 2)
            else:
                for datum in name.values():
                    datum["sale"] = round(datum.get("sale") * i, 2)

    def sell_product(self, product_name, amount):
        for name in self.storage.values():
            for good, datum in name.items():
                if product_name == good:
                    datum["total"] -= amount
                    self.income += round(((datum["sale"] - datum["price"]) * amount), 2)

    def get_income(self):
        print(self.income)


onion = Product("VEGETABLES", "Onion", 2.55)
mentos = Product("CANDIES", "Mentos", 1.11)
c = ProductStore()
c.add(onion, 100)
c.add(mentos, 55)
salmon = Product("FISH", "Salmon", 6.99)
c.add(salmon, 40)
c.add(salmon, 10)
potatoe = Product("VEGETABLES", "Potatoe", 1.98)
c.add(potatoe, 74)
orbit = Product("CANDIES", "Orbit", 1.5)
perch = Product("FISH", "Perch", 3.15)
c.add(orbit, 111)
c.add(orbit, 45)
c.add(perch, 55)
# pprint(c.storage)
c.set_discount("Salmon", 5)
# pprint(c.storage)
c.set_discount("CANDIES", 5)
pprint(c.storage)
c.sell_product("Orbit", 30)
c.get_income()
pprint(c.storage)
