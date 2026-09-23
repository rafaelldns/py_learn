print('== CHALLENGE 41 ==')
b = int(input('Enter the athletes year of birth: '))

a = 2026 - b

if a <= 9:
    print('{} years; Category: Young'.format(a))
elif a < 15:
    print('{} years; Category: Childrens'.format(a))
elif a < 20:
    print('{} years; Category: Junior'.format(a))
elif a < 21:
    print('{} years; Category: Senior'.format(a))
else:
    print('{} years; Category: Masters'.format(a))
