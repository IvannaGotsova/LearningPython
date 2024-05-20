setExample = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print(setExample)

print(len(setExample))
print(type(setExample))


print(4 in setExample)
print(4 not in setExample)

setExample.add(21)
print(setExample)

setToAdd = {22, 23, 24, 25}
setExample.update(setToAdd)
print(setExample)