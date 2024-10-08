#Arrays are Variables that store multiple values

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#no built-in support for arrays in python, lists are used instead

#methods you can use on lists/arrays
'''
append()	#Adds an element at the end of the list
clear()	#Removes all the elements from the list
copy()	#Returns a copy of the list
count()	#Returns the number of elements with the specified value
extend()	#Add the elements of a list (or any iterable), to the end of the current list
index()	#Returns the index of the first element with the specified value
insert()	#Adds an element at the specified position
pop()	#Removes the element at the specified position
remove()	#Removes the first item with the specified value
reverse()	#Reverses the order of the list
sort()	#Sorts the list
'''