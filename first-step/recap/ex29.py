print("== CHALLENGE 29 ==")
s = float(input('Enter the car speed in \033[0;34mKm: '))

if s > 80:
    print('\033[mSpeedin ticket!')
    m = (s-80) * 7
    print('The fine aumont is: \033[0;32mR${:.2f}\033[m'.format(m))
else:
    print('\033[mHave a nice trip!')
