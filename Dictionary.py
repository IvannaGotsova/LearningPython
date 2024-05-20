dictionaryExample = {
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "age": 44
}

print(dictionaryExample)
print(dictionaryExample["firstName"])

print(len(dictionaryExample))
print(type(dictionaryExample))

print(dictionaryExample.keys())
print(dictionaryExample.values())

dictionaryExample['city'] = "Sofia"
print(dictionaryExample)

print(dictionaryExample.items())

for x in dictionaryExample:
  print(x)

for x in dictionaryExample.keys():
  print(x)

for x in dictionaryExample:
  print(dictionaryExample[x])

for x in dictionaryExample.values():
  print(x)

