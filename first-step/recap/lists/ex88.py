import random
print('{:^55}'.format('CHALLENGE 88\n'))

print(55*'='+'\n'+'{:^55}'.format('PLAY MEGA-SENA')+'\n'+55*'=')

nums = [
1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,
41,42,43,44,45,46,47,48,49,50,
51,52,53,54,55,56,57,58,59,60
]

games = []
game_temp = []

while True:
    op = int(input('How many games you want to sort? '))
    if op < 0:
        print('Invalid Value. Try Again!')
    elif op > 0:
        for i in range(0,op):
            for j in range(0,6):
                random.shuffle(nums)
                game_temp.append(nums[i])
            print(f'Game {i+1}: {sorted(game_temp)}')
            games.append(sorted(game_temp[:]))
            game_temp.clear()
        break
    elif op == 0:
        break
print(55*'=')
