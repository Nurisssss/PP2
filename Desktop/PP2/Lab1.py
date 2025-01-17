#HOME
print("Hello, World!")

#Syntax
if 5 > 2:
  print("Five is greater than two!")

#Comments
print("Hello, World!") #This is a comment

#Variables
    #Python Variables
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
    #Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
    #Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
    #Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
    #Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Python Data Types
x = 5
print(type(x))

#Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#Python Casting
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Python Strings
    #Python Strings
print("Hello")
print('Hello')
    #Slicing Strings
b = "Hello, World!"
print(b[2:5])
    #Modify Strings
a = "Hello, World!"
print(a.upper())
    #Concatenate Strings
a = "Hello"
b = "World"
c = a + b
print(c)
    #Formal Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
    #Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
