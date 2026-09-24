print('{:^55}'.format('CHALLENGE 79'))

list = []

while True:
    print(55*'=')
    num = (int(input('Insert an integer: ')))
    
    op = 0

    if num in list:
        print('\nThis value have been previously added!\nTry Again!\n')
    else:
        list.append(num)
        while True:
            op = str(input('\nInteger sucefully add!!\nWant yo continue(Y/N)?')).upper()
            if op == 'N':
                break
            elif op == 'Y':
                break
            else:
                print('\nInvalid value. Try Again!\n')
    if op == 'N': break

print(55*'='+f'\nComplet list in ascending order:\n{sorted(list)}\n'+55*'=')
