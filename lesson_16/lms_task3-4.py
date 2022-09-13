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
                            if Product.name.lower() == good.lower():
                                datum["total"] = datum.get("total") + amount

    def set_discount(self, identifier, percent):
        i = (100 - percent) / 100
        for type, name in self.storage.items():
            if identifier not in type:
                for good, datum in name.items():
                    if good.lower() == identifier.lower():
                        datum["sale"] = round(datum.get("sale") * i, 2)
                        print(f'{good} become cheaper for {percent}%' )
            else:
                for good, datum in name.items():
                    datum["sale"] = round(datum.get("sale") * i, 2)
                    print(f'{good} become cheaper for {percent}%' )

    def sell(self, product_name, amount):
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
        return f"You\'ve earned ${round(self.income, 2)}"

    def get_all_products(self):
        pprint(self.storage)

    def get_product_info(self, product_name):
        for name in self.storage.values():
            for good, datum in name.items():
                if good.lower() == product_name.lower():
                    return (good, datum["total"])


class BalanceInStockError(BaseException):
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
s.sell("orbit", 50)
s.get_all_products()
s.add(orbit, 100)
s.set_discount('VEGETABLES', 5)
print(s.get_product_info('Mentos'))
