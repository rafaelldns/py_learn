print('{:^55}'.format(' CHALLENGE 75 '))

tuple = ()

for i in range ( 0, 4):
    n = int(input('\nInsert an number to add a tuple: '))
    tuple = tuple + (n, )

print(f'\nTUPLE GERATED: {tuple}')

print(f'Number of times 9 appeared: {tuple.count(9)}')
while True:
    if tuple.count(3) > 0:
        print(f'First position of number 3: {tuple.index(3)}')
        break
    else:
        print('Number 3 not appeared in tuple!')
        break

even = ()

for num in tuple:
    if num % 2 == 0:
        even = even + (num, ) 

print(f'The even numers: {even}')
