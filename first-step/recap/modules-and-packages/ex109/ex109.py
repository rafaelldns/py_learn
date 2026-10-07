import sys
import os

cur_folder = os.path.dirname(os.path.abspath(__file__))
dad_folder = os.path.dirname(cur_folder)
sys.path.append(dad_folder)

from ex111.utilities import coin
print('{:^55}'.format('CHALLENGE 109')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double of {coin.gold(n)} is: {coin.double(n, True)}')
print(f'Half of {coin.gold(n)} is: {coin.half(n)}')
print(f'10% Increase of {coin.gold(n)} is {coin.increase(n, 10, True)}')
print(f'13% Decrease of {coin.gold(n)} is {coin.decrease(n, 13, False)}')
