from random import choice
print('== CHALLENGE 28 ==')
v = [0, 1, 2, 3, 4, 5]

r = choice(v)

n = int(input("Guess the number from 0 to 5: "))

if n == r:
    print('Correct answer! The number is: {}'.format(r))
else:
    print('Wrong answer! The number is: {}'.format(r))
