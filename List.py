listExample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(listExample[4])

print(len(listExample))
print(type(listExample))

listExample[4] = 0
print(listExample[4])

listExample[4] = 5
print(listExample[4])

listExample.append(21)
listExample.append(22)
listExample.append(23)
listExample.append(24)
listExample.append(25)
print(listExample)

listExample[20] = 20.5
print(listExample)

listExample[20:21] = [21]
print(listExample)