import sys
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
dad_folder = os.path.dirname(current_folder)
sys.path.append(dad_folder)

from ex111.utilities import coin

print('{:^55}'.format('CHALLENGE 107')+'\n'+55*'=')

n = int(input('Insert a number: '))

print(f'Double: {coin.double(n)}\nHalf: {coin.half(n)}')
print(f'Increase 10%: {coin.increase(n, 10)}\nDecrease 13%: {coin.decrease(n, 13)}')
