def uniq(nums):
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums
print(uniq([1, 2, 1, 2, 3, 2]))
