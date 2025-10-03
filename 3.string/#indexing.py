# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

a = (credit_number[0])
b = (credit_number [:4]) # starting to 4th index element
c = (credit_number[5:9]) # 5th index to 9th index elements
d = (credit_number [5:]) # 5th index element to last element
e = (credit_number[-1]) # last element index
f = (credit_number[:: 3]) # starting to end elements - with 3 steps

print(f)