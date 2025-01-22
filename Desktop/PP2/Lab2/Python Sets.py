#ex1, Python Sets
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#ex2, Access Set Items
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ex3, Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#ex4, Remove Set Items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #if theres no such value, python will return error!

print(thisset)

#ex5, Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex6, Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
