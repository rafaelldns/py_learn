print('== CHALLENGE 32 ==')
nd = int(input('Enter a year: '))

n = nd

d = []
while nd > 0:
    d.insert(0, nd % 10)
    nd = nd // 10

if d[-2] == 0 and d[-1] == 0:
    if n % 400 == 0:
        print('This year is a leap year!')
    else:
        print('This year is not a leap year!')
else:
    if n % 4 == 0:
        print('This year is a leap year!')
    else:
        print('This year is not a leap year!')

#Alternative(BEST FORM):

n2 = int(input('Enter a year: '))

if n2 % 100 == 0:
    if n % 400 == 0:
            print('This year is a leap year!')
    else:
            print('This year is not a leap year!')
else:
    if n % 4 == 0:
            print('This year is a leap year!')
    else:
            print('This year is not a leap year!')
   