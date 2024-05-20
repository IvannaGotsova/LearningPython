tupleExample = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

print(tupleExample[4])
print(len(tupleExample))

tupleToAdd = (21, 22, 23, 24, 25)
tupleExample += tupleToAdd

print(tupleExample)

(one, two, three, *others) = tupleExample

print(one)
print(two)
print(three)
print(others)

