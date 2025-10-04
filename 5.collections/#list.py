# collection = single "variable" used to store multiple values
#
#            List  = [] ordered and changeable. Duplicates OK


# 1.List
fruits = ["apple", "orange", "banana", "coconut"]

typ = list()
print(type(typ))
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)


# methods
fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("pineapple"))
