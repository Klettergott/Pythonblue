x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

'''
x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variable inside a function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#global and local variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#make a global variable inside a function
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#change the value of the global variable
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#
