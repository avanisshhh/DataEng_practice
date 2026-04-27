nested_list = [[1, 2, 3], [5, 6],[4], [7, 8, 9, 10]]

sorted_list = sorted(nested_list,key=len)

print(sorted_list)

sorted_list_desc = sorted(nested_list,key=len,reverse=True)

print(sorted_list_desc)