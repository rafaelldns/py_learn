def fact(num, show=False): 
    '''
    Calculate a number factorial
    num: the number to calculate
    show: show or not the account
    '''
    if show == False:
        i = 1
        while num > 0:
            i *= num
            num -= 1
        print(i)
    
    else:
        i = 1
        while num > 1:
            i *= num
            print(f'{num}', end=' x ')
            num -= 1
        print(f'1 = {i}')


print('{:^55}'.format('CHALLENGE 102')+'\n'+55*'=')

help(fact)
fact(7, show=True)
