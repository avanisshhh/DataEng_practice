# Method 1 : Using Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = list(set(list1) & set(list2))
print(common_items)

# Method 2 : Using list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = [i for i in list1 if i in list2]
print(common_items)

# Method 3 : Using filter and lambda

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = list(filter(lambda x: x in list2,list1))
print(common_items)