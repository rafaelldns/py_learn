print('{:^55}'.format('CHALLENGE 86'))

l1= []
l2 = []
l3 = []
l_unic = []

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Insert a value for [{i},{j}]: '))
        if len(l1) <= 2:
            l1.append(num)
        elif len(l2) <= 2:
            l2.append(num)
        elif len(l3) <= 2:
            l3.append(num)

l_unic.append(l1[:])
l_unic.append(l2[:])
l_unic.append(l3[:])

for i in l_unic:
    print(f'|{i[0]} {i[1]} {i[2]}|')
