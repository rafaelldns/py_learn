# Dictionary is a data structure that allows you to store a unique key and its corresponding value

print("Dictionary creation and acess\n")
car = {
    "brand": "Honda",
    "name":"Civic",
    "year": 2021,
    "plate": "BFA2K57"
}

print(car["brand"])
print(car["plate"])
print(car["year"])
print(car["name"])

print("\nDictionary Methods\n")

# keys() : return all keys of dictionary
# values() : return all values of dictionary
# items() : return all items 
# update(new_item) : update a dictionary with a new item

person = { 
    "name" : "Marcos",
    "age" : 31,
    "city" : "Anapolis",
    "graduation" : "Civil Engineer",
    "status" : "Married"
}

print(person.keys())
print(person.values())
print(person.items())
print(person)

person.update({"profession" : "Structural Engineer"})

print(person)
