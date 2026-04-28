print("Sets creation and acess")

#Sets support a math operations: Union(|) intersection(&), difference (-), and symmetric difference(^)

set1 = {10, 20, 30, 40}
set2 = set([30, 40, 50, 60])

union = set1 | set2
print(union)

intersec = set1 & set2
print(intersec)

dif1 = set1 - set2
print(dif1)

dif2 = set2 - set1
print(dif2)

sym_dif = set1 ^ set2
print(sym_dif)

print("Methods Sets")

# add(element) : add element to set
# remove(element) : remove element, if element doesn't exist, generates an error 
# discard(element) : remove element, if element exist. If element doesn't exist, does nothing
# clear() : remove all elements of set

car = {"Fiesta", "Onix", "Cruze", "Civic"}
print(car)

car.add("Creta")
print(car)

car.remove("Cruze")
print(car)

car.discard("Accord")
print(car)

car.clear()
print(car)
