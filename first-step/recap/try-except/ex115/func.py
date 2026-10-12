cadt = dict()


def view():
    cadt['Name'] = 'Rafael', 'Jane', 'Odair', 'Eduarda'
    cadt['Age'] = '20', '49', '53', '20'
    print(50*'='+'\n'+'{:^50}'.format('REGISTERED PERSONS')+'\n'+50*'=')
    for i in cadt:
        print(f'{cadt['Name'][i]} {cadt['Age'][i]:>10}')
    print(cadt)


def add():
    input('')


def exit():
    print('Exiting system...')

    