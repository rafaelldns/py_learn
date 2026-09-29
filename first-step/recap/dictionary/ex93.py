print('{:^55}'.format('CHALLENGE 93'))

player = dict()
goals = list()

player['NAME'] = str(input('Player Name: '))
matches = int(input(f'How Many Matches {player["NAME"]} Played? '))

for i in range (0, matches):
    goals.append(int(input(f'How many goals scored in the match {i+1}: ')))

player['GOALS'] = goals
player['TOTAL'] = sum(goals)

print(55*'=' + f'\n{player}\n' + 55*'=')

for i, j in player.items():
    print(f'{i} = {j}')

print(55*'=')
print(f'The player {player["NAME"]} played {matches} matches: ')
for i, j in enumerate(goals):
    print(f'    =>In match {i+1}: Scored {j} goals')
print(f'It was a total of {player["TOTAL"]} goals')
