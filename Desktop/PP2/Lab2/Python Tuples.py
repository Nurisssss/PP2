#Python Tuples
#ex1, Python Tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#ex2, Access Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#ex3, Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ex4, Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#ex 5, Loop Tuples
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#ex6, Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
