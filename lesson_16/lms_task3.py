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
            else:
                for datum in name.values():
                    datum["sale"] = round(datum.get("sale") * i, 2)

    def sell_product(self, product_name, amount):
        for name in self.storage.values():
            for good, datum in name.items():
                if product_name.lower() == good.lower():
                    datum["total"] -= amount
                    inc = (datum["sale"] - datum["price"]) * amount
                    self.income += inc
                    print(f'You\'ve became richer for ${round(inc, 2)}')

    def get_income(self):
        return f'${round(self.income, 2)}'
    
    def get_all_products(self):
        pprint(self.storage)

    def get_product_info(self, product_name):
        for name in self.storage.values():
            for good, datum in name.items():
                if good.lower() == product_name.lower():
                    return (good, datum['total'])



s = ProductStore()
s.get_all_products()