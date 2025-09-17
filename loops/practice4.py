# 4. Reverse a String
# Problem: Reverse a string using a loop.

string = input("String : ")

reverse_str = ""

        #   "abc"
for chr in string :
    reverse_str = chr + reverse_str
                # "a"
	            # "b" + "a" = "ba"
	            # "c" + "ba" = "cba"
print(f"Your Reverse String - {reverse_str}." )