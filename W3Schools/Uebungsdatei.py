"""
Kommentar in mehreren Zeilen ;D
"""
x, y, z = "Orange", "Banana", "Cherry"

#global makes an variable available inside aswell as outside of the function
def function():
    global ha
    ha = 4
print(ha)

#printet den Datentypen der Variable = in dem Fall 'int' oder auch Float,string,boolean,list,tuple
print(type(ha))
f = ["tower", "tree"] #type list
g = ("tower", "tree") #type tuple
x = {"name" : "John", "age" : 36} #type dict

x = 5
x = float(x)
x = int(x)
x = " hello world "
print(len(x))

first = x[0] #first character of string
last = x[-1] #last character of string
index2bis4 = x[2:5] #3,4,5 character of string

x = x.upper() #convert string to uppercase
x = x.lower() #convert string to lowercase
x = x.strip() #strips the empty spaces at the beginning and end
x = x.replace("H", "J") #replaces character with other character

print(7 > 4)
#True if < then False

print(bool("abc"))
#True
print(bool(0))
#False

fruits = ["apple", "banana", "cherry"]
fruits.append("lauch")
fruits.insert(1,"lemon")                #fügt lemon an zweiter Stelle der Liste ein
fruits.remove("banana")
fruits.pop() #removes and return item at given index, wenn die Klammern leer sind automatisch das letzte aus der Liste

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits.remove("banana")
fruits.discard("banana")

#dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model")) #Mustang


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") #gibt aus und löscht "model"

car.clear() #löscht alles aus dem dictionary

a = 2
b = 5
print("YES") if a == b else print("NO")

a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition
def my_function(*kids):
    print("The youngest child is " + kids[2])

#If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition
def my_function(**kid):
    print("His last name is " + kid["lname"])

#create a class and a object of said class
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):
    a = 2


class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")
x.printname()


#modules
#What is the correct syntax of printing all variables and function names of the "mymodule" module?
import time
print(dir(time))


from time import time