from random import choice
print('== CHALLENGE 68 ==\n')

print(25*'=-')
txt = 'LETS PLAY ODDS OR EVENS'
print(f'|{txt: ^48}|')
print(25*'=-')

n = [0,1,2,3,4,5,6,7,8,9,10]
count_win = 0
res = 0
end ='GAME OVER'

while True:
    choic = str(input('Odd or even(O/E)? ')).upper()
    num = int(input('Enter the value: '))
    print(25*'=-')
    pc = choice(n)
    res = pc + num
    if res % 2 == 0:
        print(f'You play {num}, the PC play {pc}. Total {res} its EVEN!!')
        if choic == 'E':
            print('You Win!!\n' + 25*'=-')
            count_win +=1
        elif choic == 'O':
            print('You Lose!\n' + 25*'=-' + f'\n{end: ^50}!\nYou won {count_win} times!')
            break
    else:
        print(f'You play {num}, the PC play {pc}. Total {res} its ODD!!')
        if choic == 'O':
            print('You Win!!\n' + 25*'=-')
            count_win +=1
        elif choic == 'E':
            print('You Lose!\n' + 25*'=-' + f'\n\n{end: ^50}\n\nYou won {count_win} times!')
            break
print('\n\nFinishing...\n')
