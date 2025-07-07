cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}

s = 0

for value in cart.values():
    s += value['price']*value['quantity']

print(s)