print("== CHALLENGE 29 ==")
s = float(input('Enter the car speed in Km: '))

if s > 80:
    print('Speedin ticket!')
    m = (s-80) * 7
    print('The fine aumont is: R${:.2f}'.format(m))
else:
    print('Have a nice trip!')
