import menu, time
cadt = dict()


def view():
    print(50*'='+'\n'+'{:^50}'.format('REGISTERED PERSONS')+'\n'+50*'=')
    try:
        with open('persons.txt', 'r', encoding='utf-8') as recorder:
            for l in recorder:
                l = l.replace('\n', '')
                if not l.strip():
                    continue
                data = l.split(';')
                if len(data) == 2:
                    print(f'{data[0]:<40} {data[1]} years')
    except FileNotFoundError:
        print('The archive doesnt exist, first insert a person!')
        time.sleep(2)
        return menu.menu()


def add(name, age):
    print(50*'='+'\n'+'{:^50}'.format('NEW REGISTER')+'\n'+55*'=')
    try: 
        with open('persons.txt', 'a', encoding='utf-8') as recorder:
            recorder.write(f'{name}, {age}\n')
        print(f'New register of {name} have been add!')
        time.sleep(2)
        return menu.menu()
    except Exception as e:
        print(f'ERROR: {e}')
        time.sleep(2)
        return menu.menu()



def exit():
    print('Exiting system...')

    