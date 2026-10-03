def readint(msg):
    num = input(msg)
    
    while num.isdigit() == False:
        print('\033[31mERROR! Insert a valid integer.\033[0m')
        num = input(msg)
    return int(num)


print('{:^55}'.format('CHALLENGE 104')+'\n'+55*'=')

n = readint('Insert a integer: ')
print(f'You insert a integer: {n}')
