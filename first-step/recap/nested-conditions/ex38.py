print('== CHALLENGE 38 ==')
n1 = int(input('Insert a first integer: '))
n2 = int(input('Insert a second integer: '))

if n1>n2:
    print('The first value {} is largest'.format(n1))
elif n2>n1:
    print('The second value {} is largest'.format(n2))
else:
    print('There is no greater value, the two are the same!')
