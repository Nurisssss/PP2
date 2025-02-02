def has33(lst):
    for i in range(0, len(lst)-1):
        if lst[i] == 3 and lst[i+1] == 3:
            return True
    return False
print(has33([1, 3, 3]))
print(has33([1, 3, 1, 3]))
print(has33([3, 1, 3]))
