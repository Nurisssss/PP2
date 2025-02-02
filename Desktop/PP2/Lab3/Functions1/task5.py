from itertools import permutations
def all_perms(s):
    s = ''.join(sorted(s))
    perms = [''.join(p) for p in permutations(s)]
    print(perms)
all_perms(input("Enter string: "))
