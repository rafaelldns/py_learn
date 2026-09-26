print('{:^55}'.format('CHALLENGE 86'))

l1= []
l2 = []
l3 = []
l_unic = []
even = []

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Insert a value for [{i},{j}]: '))
        if num % 2 == 0:
            even.append(num)
        if len(l1) <= 2:
            l1.append(num)
        elif len(l2) <= 2:
            l2.append(num)
        elif len(l3) <= 2:
            l3.append(num)

l_unic.append(l1[:])
l_unic.append(l2[:])
l_unic.append(l3[:])

s2 = 0

for i in l_unic:
    print(f'|{i[0]} {i[1]} {i[2]}|')
    s2 += i[2]

se = sum(even)

big2= 0

for i in l2:
    if big2 < i:
        big2 = i

print(f'''
The sum of all even numbers inserted: {se} 
The sum of value in third column: {s2}
The biggest value in second line: {big2}
''')
