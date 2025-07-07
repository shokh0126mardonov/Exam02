numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]

result = list(filter(lambda nums: nums['value'] > 0,numbers))