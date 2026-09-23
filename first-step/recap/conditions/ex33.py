print('== CHALLENGE 33 ==')
n1, n2, n3 = map(float, input('Enter three numbers:\n').split())

cores = {'blue':'\033[0;34m', 'clean':'\033[m', 'red':'\033[0;31m'}
if n1 > n2 and n1 > n3:
    print('{}{}{} is the largest number'.format(cores['blue'],n1,cores['clean']))
    if n2 < n3:
        print('{}{}{} is the smallest number'.format(cores['red'],n2,cores['clean']))
    else: 
        print('{}{}{} is the smallest number'.format(cores['red'],n3,cores['clean']))
elif n2 > n3:
    print('{}{}{} is the largest number'.format(cores['blue'],n2,cores['clean']))
    if n1 < n3:
        print('{}{}{} is the smallest number'.format(cores['red'],n1,cores['clean']))
    else:
        print('{}{}{} is the smallest number'.format(cores['red'],n3,cores['clean']))
else: 
    print('{}{}{} is the largest number'.format(cores['blue'],n3,cores['clean']))
    if n1 > n2:
        print('{}{}{} is the smallest number'.format(cores['red'],n2,cores['clean']))
    else:
        print('{}{}{} is the smallest number'.format(cores['red'],n1,cores['clean']))
