# collection = single "variable" used to store multiple values
#
#            Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# 3.tuple
fruits = ("apple", "orange", "banana", "coconut")

typ = tuple()
print(type(typ))
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)


# methods
print(fruits.index("apple"))
print(fruits.count ("coconut"))