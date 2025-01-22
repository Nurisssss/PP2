#1 ex
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2 ex
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3 ex
print(bool("Hello"))
print(bool(15))

#4 ex
#print(bool("Hello"))
print(bool(15))

#5 ex
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6 ex
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7 ex
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8 ex
def myFunction() :
  return True

print(myFunction())

#9 ex
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#10 ex
x = 200
print(isinstance(x, int))
