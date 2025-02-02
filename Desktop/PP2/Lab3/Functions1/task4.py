
def filter_prime(mylist):
    newlist = []
    for i in mylist:
        ok = 1
        for j in range(2, i):
            if i%j == 0:
                ok = 0
                break
        if ok==1:
            newlist.append(i)
    return newlist

mylist = list(map(int, input("Enter elements separated by space: ").split()))
print("Filtered list: ", filter_prime(mylist))
