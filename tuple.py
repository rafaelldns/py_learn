print("Tuple cration and acess")
point = (25, 37, 42)
print(point[0])
print(point[2])
print(point[1])

# count(element) : number of times the element appears
# index(element) : index of the first element's apearance in the tuple, can specify the start and end of the search
# len(tuple) : return the length

print("\nTuple Methods")

tuple = (14, 15, 17, 14, 21, 14, 15, 14)

print (tuple.count(14))
print (tuple.index(14))
print (tuple.index(15))
print (tuple.index(14, 1))
print (tuple.index(14, 4, 6))
print (len(tuple))
