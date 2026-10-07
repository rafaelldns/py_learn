import coin3
print('{:^55}'.format('CHALLENGE 109')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double of {coin3.gold(n)} is: {coin3.double(n, True)}')
print(f'Half of {coin3.gold(n)} is: {coin3.half(n)}')
print(f'10% Increase of {coin3.gold(n)} is {coin3.increase(n, 10, True)}')
print(f'13% Decrease of {coin3.gold(n)} is {coin3.decrease(n, 13, False)}')
