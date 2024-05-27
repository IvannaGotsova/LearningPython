dictionaryExample = {
  "first_name": "Ivan",
  "second_name": "Petar",
  "third_name": "Petar",
  "fourth_name": "Ivan",
  "fifth_name": "Ivan",
  "sixth_name": "Dimitar"
}


def check_condition(value):
    if value == "Ivan":
        return '3'
    elif value == "Petar":
        return '2'
    else:
        return '1'


specific_name = {key: value for (key, value) in dictionaryExample.items()}
print(specific_name)

specific_name = {key: value for (key, value) in dictionaryExample.items() if value == "Ivan"}
print(specific_name)

specific_name = {key: check_condition(value) for (key, value) in dictionaryExample.items()}
print(specific_name)

