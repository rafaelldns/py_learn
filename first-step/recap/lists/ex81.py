print('{:^55}'.format('CHALLENGE 81\n'))

list = []

while True:
    print(55*'=')
    list.append(int(input('Insert an value: ')))
    
    op = 0

    while True:
        op = str(input('Want to continue? [Y/N]')).upper()        
        if op == 'N' or op == 'Y':
                break    
        elif op != 'Y':
             print('Invalid Value. Try Again!')

    if op == 'N': break

    

rev_list = sorted(list, reverse=True)
five = 0

if 5 in list:
    five = 'is'
else:
    five = 'is not'

print(f'''
Were inserted {len(list)} numbers!
LIst in decreasin order: {rev_list}
The Number 5 {five} in the list
''')
