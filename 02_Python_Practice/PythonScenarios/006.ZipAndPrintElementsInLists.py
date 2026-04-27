list1 = [10,20,30]
list2 = ['India','UK','US']

for i,j in zip(list1,list2):
    print(i,j)


list1 = [10,20,30]
list2 = ['India','UK','US']

for item in zip(list1,list2):
    print(item)

list1 = [10,20,30]
list2 = ['India','UK','US']

print(list(zip(list1,list2)))


list1 = [10,20,30,40]
list2 = ['India','UK','US']

print(list(zip(list1,list2)))