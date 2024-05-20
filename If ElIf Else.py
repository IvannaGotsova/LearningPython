one = 1
two = 2
three = 3


if one > two and one > three:
    print("One is bigger")
elif one < two and one < three:
    print("One is smaller")
else:
    print("Not of the abpve")

print("One is bigger") if one > two and one > three else print("One is smaller") if one < two and one < three else print("Not of the abpve")