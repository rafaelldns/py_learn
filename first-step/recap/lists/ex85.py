print('{:^55}'.format('CHALLENGE 85'))

ev_list = []
od_list = []
list_unic = []

for i in range(1, 8):
    comp = (int(input(f'Insert {i}º Number: ')))
    if comp % 2 == 0:
        ev_list.append(comp)
    else: od_list.append(comp)

list_unic.append(sorted(ev_list[:]))
list_unic.append(sorted(od_list[:]))

print(f'''
The even list numbers inserted is:\n{list_unic[0]}
The odd list numbers inserted is:\n{list_unic[1]}
''')
