words = "salom salom dunyo".split()

new_dict = {}

for word in words:
    if word not in new_dict:
        new_dict[word] = 1
    else:
        new_dict[word] += 1

print(new_dict)