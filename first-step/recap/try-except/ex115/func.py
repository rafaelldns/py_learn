import menu, time
cadt = dict()


def view():
    cadt['Name'] = 'Rafael', 'Jane', 'Odair', 'Eduarda'
    cadt['Age'] = '20', '49', '53', '20'
    print(50*'='+'\n'+'{:^50}'.format('REGISTERED PERSONS')+'\n'+50*'=')
    for i in range(len(cadt['Name'])):
        print(f"{cadt['Name'][i]:<40} {cadt['Age'][i]} years")
    time.sleep(2)
    return menu.menu()


def add():
    input('')


def exit():
    print('Exiting system...')

    