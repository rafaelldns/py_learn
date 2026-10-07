import coin2
print('{:^55}'.format('CHALLENGE 108')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double of {coin2.gold(n)} is: {coin2.gold(coin2.double(n))}')
print(f'Half of {coin2.gold(n)} is: {coin2.gold(coin2.half(n))}')
print(f'10% Increase of {coin2.gold(n)} is {coin2.gold(coin2.increase(n))}')
print(f'13% Decrease of {coin2.gold(n)} is {coin2.gold(coin2.decrease(n))}')
