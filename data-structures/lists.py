#Methods
car_brand = ["Volkswagen", "Fiat", "Chevrolet"]
print("Inicial brand list\n", car_brand)

print("Append")
car_brand.append("Honda")
print(car_brand)

print("Insert")
car_brand.insert(0, "Hyundai")
print(car_brand)

print("Remove")
car_brand.remove("Volkswagen")
print(car_brand)

print("Pop")
removed_brand = car_brand.pop(2)
print(car_brand)
print(removed_brand)

print("Sort")
car_brand.sort()
print(car_brand)

print("Reverse")
car_brand.reverse()
print(car_brand)


print("Comprehension List")
num = [1, 2, 3, 4, 5, 6, 7]
power  = [ x ** 2 for x in num if x % 2 != 0]
print(power)
