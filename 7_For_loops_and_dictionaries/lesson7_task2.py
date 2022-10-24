stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

final_price = {}
for i, j in zip(stock, prices):
    final_price[i] = stock.get(i) + prices.get(j)
    print(i, ':', final_price[i])
