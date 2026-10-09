import os
import sys

cur_fold = os.path.dirname(os.path.abspath(__file__))
dad_fold = os.path.dirname(cur_fold)
sys.path.append(dad_fold)

from ex111.utilities import data, coin

print('{:^55}'.format('CHALLENGE 112'))

msg = 'Insert a Value'
val = data.read_cash(msg)
coin.resume(val, 35, 22)
