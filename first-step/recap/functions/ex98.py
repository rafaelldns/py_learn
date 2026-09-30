import time

print('{:^55}'.format('CHALLENGE 98'))

def counter(init, end, step):
    if step == 0:
            step = 1
    aux = abs(step)
    
    print('\n'+55*'='+f'\nCount {init} to {end}, {aux} by {aux}')
    time.sleep(1)

    if init < end:
        count = init
        while count <= end:
            time.sleep(1)
            print(f"{count} ", end='', flush=True)
            count += aux
    else: 
        count = init
        while count>= end:
            time.sleep(1)
            print(f"{count} ", end='', flush=True)
            count -= aux


counter(1,10,1)
counter(10,0,2)

print('\n'+55*'='+'\n\nYour turn to performe the count: ')
i = int(input('Init: '))
e = int(input('End: '))
s = int(input('Step: '))

counter(i,e,s)
