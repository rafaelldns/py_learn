print('{:^55}'.format('CHALLENGE 95') + '\n' +55*'=')

player = dict()
goals = list()
players_list = list()

while True:
    player['NAME'] = str(input('Player Name: '))
    matches = int(input(f'How Many Matches {player["NAME"]} Played? '))

    for i in range (0, matches):
        goals.append(int(input(f'How many goals scored in the match {i+1}: ')))

    temp_goals = goals.copy()
    goals.clear()

    player['GOALS'] = temp_goals
    player['TOTAL'] = sum(temp_goals)

    temp = player.copy()

    players_list.append(temp)
    player.clear()

    op = 0
    while True: 
        op = str(input('Want to continue? [Y/N]')).upper()
        if op == 'Y' or op =='N': break
        else: print('Invalid Value. Try Again!')
    if op == 'N': break
    print(55*'-')

print(55*'='+f'\n{"CODE":>4} {"NAME":<15} {"GOALS":<20} {"TOTAL":<1}\n'+55*'-')

for i, j in enumerate(players_list):
    print(f'{i:>4} {j["NAME"]:<15} {str(j["GOALS"]):<20} {j["TOTAL"]:<1}')

while True:
    print(55*'=')
    op = int(input('Show data for which player? [999 to stop] '))
    if op == 999: break
    elif op < 0 or op > (len(players_list)-1): 
            print(f'ERROR! doesnt exist player CODE {op}! Try Again!')
    else:
        for i, j in enumerate(players_list[op]["GOALS"]):
            print(f'Match {i+1} scored {j} goals.')
