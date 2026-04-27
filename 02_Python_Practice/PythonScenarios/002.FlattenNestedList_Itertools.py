from itertools import chain
nested_list = [[1,2,3],[4,5],[5,6,7]]
flatten_list = list(chain.from_iterable(nested_list))
print(flatten_list)