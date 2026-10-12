import func

def menu():
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
    else:
        if op == 1:
            func.view()
        
        if op == 2:
            func.add()
        if op == 3:
            func.exit()