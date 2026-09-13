from random import choice
print('== CHALLENGE 28 ==')
v = [0, 1, 2, 3, 4, 5]

r = choice(v)

n = int(input("Guess the number from \033[0;33m0 to 5\033[m: "))

if n == r:
    print('\033[0;32mCorrect answer!\033[m The number is: {}'.format(r))
else:
    print('\033[0;31mWrong answer!\033[m The number is: {}'.format(r))
