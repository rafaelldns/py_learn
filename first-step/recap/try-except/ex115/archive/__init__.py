def archive(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def creat(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('\033[mERROR IN CREATE THE ARCHIVE!\033[m')
    else:
        print(f'Archive {name} suscefull created!')


def readArc(arc):
    try:
        a = open(arc, 'rt')
    except:
        print('Error in opening')
    else:
        print(50*'='+'\n'+'{:^50}'.format('CADASTERED PERSONS')+'\n'+50*'=')
        for li in a:
            data = li.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<40}{data[1]:>3} years')
    finally:
        a.close()


def addArc(arc, n= 'Unknow',age= 0):
    try:
        a = open(arc, 'at')
    except:
        print('Error in opening')
    else: 
        try:
            a.write(f'{n};{age}\n')
        except:
            print('Error in write data')
        else:
            print(f'New registration of {n} add!')
    finally:
        a.close()
    