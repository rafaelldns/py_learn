import os
import sys

cur_fold = os.path.dirname(os.path.abspath(__file__))
dad_fold = os.path.dirname(cur_fold)
sys.path.append(dad_fold)

from ex111.utilities import coin
print('{:^55}'.format('CHALLENGE 109')+'\n'+55*'=')

n = int(input('Insert a number: '))
coin.resume(n, 80, 35)
