# Method 1 : Using dictionary
items = [1,2,2,3,3,3,4]

freq_dict = {}

for item in items:
    freq_dict[item] = freq_dict.get(item,0) + 1
print(freq_dict)

freq_dict = {1: 1, 2: 2, 3: 3, 4: 1}
freq_dict.get(7,0)


# Method 2 : Using collections

from collections import Counter

items = [1,2,2,3,3,3,4]

freq = Counter(items)
print(freq)