def has33(lst):
    for i in range(0, len(lst)-1):
        if lst[i] == 3 and lst[i+1] == 3:
            return True
    return False
def uniq(nums):
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums
print(has33([0, 3, 4, 3]))
print(has33([0, 3, 3, 4]))
print(uniq([0, 3, 4, 3]))
