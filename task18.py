numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

square_values = list(map(lambda nums: {'value' : nums['value']},numbers))

print(square_values)