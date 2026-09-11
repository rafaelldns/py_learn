print('== CHALLENGE 33 ==')
n1, n2, n3 = map(float, input('Enter three numbers:\n').split())

if n1 > n2 and n1 > n3:
    print('{} is the largest number'.format(n1))
    if n2 < n3:
        print('{} is the smallest number'.format(n2))
    else: 
        print('{} is the smallest number'.format(n3))
elif n2 > n3:
    print('{} is the largest number'.format(n2))
    if n1 < n3:
        print('{} is the smallest number'.format(n1))
    else:
        print('{} is the smallest number'.format(n3))
else: 
    print('{} is the largest number'.format(n3))
    if n1 > n2:
        print('{} is the smallest number'.format(n2))
    else:
        print('{} is the smallest number'.format(n1))
