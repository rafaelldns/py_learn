import func
from archive import *
from time import sleep

def menu(arc):
    while True:
        print(50*'='+'\n'+'{:^50}'.format('MAIN MENU')+'\n'+50*'=')
        print('\033[0;33m1 -\033[0;34mView registered people')
        print('\033[0;33m2 -\033[0;34mRegister new person')
        print('\033[0;33m3 -\033[0;34mExit system\033[m')
        print(50*'=') 
        op = int(input('Your option: '))   

        try:
            op > 3 or op < 1
        except Exception:
            print('Insert a valid option:')
        if op == 1:
            readArc(arc)
        elif op == 2:
            print(50*'='+'\n'+'{:^50}'.format('NEW REGISTRATION')+'\n'+'='*50)
            n = input('Name: ')
            a = func.readint('Age: ')
            addArc(arc, n, a)
        elif op == 3:
            print(50*'-'+'\n'+'{:^50}'.format('Exiting...')+'\n'+50*'-')
            break
        else: 
            print(50*'-'+'\n'+'\033[31mERROR: Insert a valid option!\033[m')
        sleep(2)

