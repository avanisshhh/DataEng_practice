# Method 1 : Using List comprehension
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
len_list= [len(sublist) for sublist in nested_list]
print(len_list)

# Method 2: Using for loop

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
len_list = []
for sublist in nested_list:
    len_list.append(len(sublist))

print(len_list)

# Method 3: Using Map

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
len_list = list(map(len,nested_list))
print(len_list)

# Method 4 : Using Dictionary
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

len_dict={i:len(sublist) for i,sublist in enumerate(nested_list)}
print(len_dict)