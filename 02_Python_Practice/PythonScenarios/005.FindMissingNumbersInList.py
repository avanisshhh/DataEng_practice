# Method 1 : Using Set
nums = [1, 2, 4, 6, 7]
start = 1
end = 7

missing_nums = list(set(range(start,end+1)) - set(nums))

print(missing_nums)

# Method 2: List Comprehension

nums = [1, 2, 4, 6, 7]
start = 1
end = 7

missing_nums = [i for i in range(start,end+1) if i not in nums]
print(missing_nums)

# Method 3: Using Max & Min

nums = [1, 2, 4, 6, 7]

missing_nums = [i for i in range(min(nums),max(nums)+1) if i not in nums]
print(missing_nums)