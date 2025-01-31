# PYTHON BOOLIANS
# print(11 > 8)
# print(11 == 8)
# print(11 < 8)

# a = 350
# b = 21
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("HI"))
# print(bool(16))

# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

# def hisFunction() :
#   return True
# print(hisFunction())

# x = 335
# print(isinstance(x, int))

# PYTHON OPERATORS
# print(25 + 5)

# print(200 + 6 * 2)

# PYTHON LISTS
# mylist = ["watermelon", "melon", "grapes"]

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# list1 = ["apple", "banana", "cherry"]
# list2 = [2, 4, 1, 8, 9]
# list3 = [True, False, False]

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

#PYTHON TUPLES
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

#PYTHON SETS
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# PYTHON DICT
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2016

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1963
# }
# thisdict.pop("model")
# print(thisdict)

# for x in thisdict.values():
#   print(x)

#PYTHON IFELSE
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 225
# b = 30
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

#PYTHON WHILE
# i = 3
# while i < 6:
#   print(i)
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

#PYTHON FOR
# fruits = ["grapes", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")