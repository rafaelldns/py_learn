import random
import time

print('{:^55}'.format('CHALLENGE 91'))

players = dict()

for i in range(0,4):
    players[f'Player {i+1}'] = (random.randint(1,6))

print(55*'='+'\nSorted values: ')

for i, j in players.items():
    time.sleep(1)
    print(f'    The {i} got {j}')

players_ord = dict(sorted(players.items(), key=lambda item: item[1]))

print(55*'='+'\nPlayers Ranking:')
count = 1
for i, j in players.items():
    time.sleep(1)
    print(f'    {count}º Place: {i} with {j}')
    count += 1
