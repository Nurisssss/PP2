def histogram(nums):
    for i in nums:
        for j in range(0, i-1):
            print("*",end="")
        print("*")
histogram([4, 9, 7])
