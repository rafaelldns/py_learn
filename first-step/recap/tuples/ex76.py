print('{:^55}'.format(' CHALLENGE 76 '))

items = ('RAM Memory', 600, 'Graphics Card', 2500, 'SSD nvme', 749.99, 'Monitor', 600, 'Processor', 1000,
'Font', 350, 'Cabinet', 250, 'Water Cooler', 280, 'HD', 300, 'Mouse', 125, 'Keyboard', 240, 'Mousepad', 60)

print(55*'=')
print('{:^55}'.format('PRICE LIST'))
print(55*'=')

for i in range(0, len(items), 2):
    print(f'{items[i]:.<46}R${items[i+1]:.2f}')
