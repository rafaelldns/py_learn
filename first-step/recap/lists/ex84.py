print('{:^55}'.format('CHALLENGE 84'))

peo_kg = list()
data = list()

while True:
    print(55*'=')
    data.append(str(input('Name: ')))
    data.append(float(input('Weight: ')))
    peo_kg.append(data[:])
    data.clear()

    op = 0
    while True:
        op = str(input('Want to Continue? [Y/N]')).upper()
        if op == 'Y' or op == 'N':
            break
        else:print('Invalid Value. Try Again!')
    if op == 'N': break

big_kg = []
smal_kg = []

for i in peo_kg:
    if i[1] > 90:
        big_kg.append(i)
    elif i[1] < 80:
        smal_kg.append(i)

print(f'Were registered {len(peo_kg)}')

print('\nList of heavier people:')
for i in big_kg:
    print(f'{i[0]}: {i[1]}Kg')
print('\nList of lighter people:')
for i in smal_kg:
    print(f'{i[0]}: {i[1]}Kg')
