print('== CHALLENGE 39 ==')
b = int(input('Insert your year of birth: '))

a = 2026 - b

if a > 18:
    f = a - 18
    print('Youve already missed your enlistment deadline by {} years.'.format(f))
elif a < 18:
    f = 18 - a
    print('You have {} years left until your enlistment.'.format(f))
else: 
    print('You are in your registration year.')
