nested_list = [[1,2,3],[4,5],[5,6,7]]
flatten_list = [i for sublist in nested_list for i in sublist]
print(flatten_list)