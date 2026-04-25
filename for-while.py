materials = ["Books", "Rubber", "Pen", "Pencil"]

for material in materials:
    print (material)

print("Using for num")
for num in range(1, 4):
    print (num * 3)

print ('Using while num')
contador = 1
while contador <= 3:
    print (contador * 3)
    contador += 1

print ("Using while if break")
count = 1
while True:
    print (count)
    count +=1

    if count == 11:
        break

print ("Using continue to print pair number")
for i in range (15):
    if i % 2 != 0:
        continue
    print (i)

print("Using pass for reserv a block to implement later")
for n in range (5):
    pass
#reservado para que seja implementado depois