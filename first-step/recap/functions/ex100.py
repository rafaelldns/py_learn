from time import sleep
from random import randint

print('{:^55}'.format('CHALLENGE 100'))

lis = list()

def sort():
    print('\n'+55*'='+'\nSorting 5 values from 1 to 10')
    
    for i in range(0,5):
        value = randint(1, 10)
        print(f'{value} ', end="" , flush=True)
        sleep(0.5)
        lis.append(value)


def sumEven(lt):
    sum_lt = 0
    
    for i in lt:
        if i % 2 == 0:
            sum_lt += i
    
    print(f'\nIn the list: {lt}\nThe sum is: {sum_lt}')    


sort()
sumEven(lis)
