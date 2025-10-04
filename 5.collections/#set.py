# collection = single "variable" used to store multiple values
#           
#            Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates           


# 2.set
fruits = {"apple", "orange", "banana", "coconut"}

typ = set()
print(type(typ))
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)


# methods
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)