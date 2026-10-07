import sys
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
dad_folder = os.path.dirname(current_folder)
sys.path.append(dad_folder)

from ex111.utilities import coin
print('{:^55}'.format('CHALLENGE 108')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double of {coin.gold(n)} is: {coin.gold(coin.double(n))}')
print(f'Half of {coin.gold(n)} is: {coin.gold(coin.half(n))}')
print(f'10% Increase of {coin.gold(n)} is {coin.gold(coin.increase(n,10))}')
print(f'13% Decrease of {coin.gold(n)} is {coin.gold(coin.decrease(n,13))}')
