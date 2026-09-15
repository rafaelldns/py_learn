print('== CHALLENGE 52 ==')
n = int(input('Insert a integer: '))

div = 0

for i in range(1,n + 1):
    if n % i == 0:
        div +=1
if div == 2:
    print('Its a prime number!')
else:
    print('Itsnt a prime number!')
