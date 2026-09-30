from random import randint
from time import sleep
print('{:^55}'.format('CHALLENGE 100'))

lst = list()

def sort():
    print('\n'+55*'='+'\nSorting 5 values from 1 to 10:')
    for i in range(0,5):
        s = randint(1,10)
        print(f'{s} ', end='' , flush=True)
        lst.append(s)
        sleep(0.5)


def sum_even(nums):
    print('\n'+55*'='+f'\nSum the even values of list: {nums}')
    even_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
    print(f'The Sum is: {even_sum}')


sort()
sum_even(lst)
