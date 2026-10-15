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
        print(a.readlines())