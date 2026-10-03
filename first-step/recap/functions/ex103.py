def record(name, goals):
    if name == '':
        print('The Player <unknown> ', end='')
    else:
        print(f'The Player {name} ', end='')
    if goals == '':
        print('scored 0 goals in the championship.\n')
    else:
        print(f'scored {goals} goals in the championship.\n')


print('{:^55}'.format('CHALLENGE 103')+'\n'+55*'=')

nm = input('Insert a Player Name: ')
gs = input('Insert a Number of Goals: ')

record(nm,gs)
