print('== CHALLENGE 31 ==')
km = float(input('Enter the travel distance in Km: '))

if km <= 200:
    v = km * 0.5
    print('The travel price is: R${}'.format(v))
else:
    v = km * 0.45
    print('The travel price is: R${}'.format(v))
