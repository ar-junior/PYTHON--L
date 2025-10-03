# format specifiers = {value:flags} format a value based on what
#                     flags are inserted



# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces in front of them
# :03 = allocate and zero pad that many spaces in front of them
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# := insert a space before positive numbers
# :, = comma separator


price1 = 34000.8882
price2 = -2000.44
price3 = 120000000.9

print(f"price1 {price1:,}")
print(f"price2 {price2:,}")
print(f"price3 {price3:,}")