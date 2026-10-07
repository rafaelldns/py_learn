import coin
print('{:^55}'.format('CHALLENGE 107')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double: {coin.double(n)}\nHalf: {coin.half(n)}')
print(f'Increase 10%: {coin.increase(n)}\nDecrease 13%: {coin.decrease(n)}')