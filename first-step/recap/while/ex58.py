from random import choice
print('== CHALLENGE 58 ==')

print('\n=======GAME=======\nGuess the number from 0 to 10:')

num = [0, 1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]
pc_num = choice(num)
res = -1
attempts = 0

while res != pc_num:
    res = int(input('\nChoice a number: '))
    attempts +=1
    if res == pc_num:
        print('\nYou got it right!\nYou need {} attempts!'.format(attempts))
    else: 
        print('Wrong answer! Try again!')
print('\nSucess!')
