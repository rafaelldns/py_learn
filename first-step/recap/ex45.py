from random import choice

print('== CHALLENGE 45 ==')
r = 'ROCK'
p = 'PAPER'
s = 'SCISSORS'

j = [r, p, s]

print('Lets play JOKENPO:')
c = str(input('CHOOSE: ROCK, PAPER or SCISSORS? ')).strip()

c = c.upper()

b = (choice(j))

if 'ROCK' in c:
    print('Computer choose: {} x You choose: {}'.format(b, c))
    if 'ROCK' in b:
        print('DRAW!!!')
    elif 'PAPER' in b:
        print('LOSE!!!')
    elif 'SCISSORS' in c:
        print('WON!!!')
elif 'PAPER' in c:
    print('Computer choose: {} x You choose: {}'.format(b, c))
    if 'ROCK' in b:
        print('WON')
    elif 'PAPER' in b:
        print('DRAW!!!')
    elif 'SCISSORS' in b:
        print('LOSE!!!')
elif 'SCISSORS' in c: 
    print('Computer choose: {} x You choose: {}'.format(b, c))
    if 'ROCK' in b:
        print('LOSE!!!')
    elif 'PAPER' in b:
        print('WON!!!')
    elif 'SCISSORS' in b:
        print('DRAW!!!')
else:
    print('\nInvalid value! Try Again...')
    