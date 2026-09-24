print('{:^55}'.format('CHALLENGE 82'))

list = []
even_list = []
odd_list = []

while True:
    print(55*'=')
    list.append(int(input('Insert an Number: ')))
    op = 0

    while True:
        op = str(input('Want to continue? [Y/N]')).upper()
        if op == 'Y' or op == 'N':
            break
        else:
            print('Invalid Value. Try Again!')
    if op == 'N': break

for num in list:
    if num % 2 == 0:
        even_list.append(num)
    else: 
        odd_list.append(num)

print(f'''
The Final list is: {sorted(list)}
The Even list is: {sorted(even_list)}
The Odd list is: {sorted(odd_list)}
''')
