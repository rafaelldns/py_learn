print('== CHALLENGE 49 ==')
n = int(input('Insert a number: '))

print('Printing the multiplication table of {}'.format(n))
for i in range(1,10):
    t = n*i
    print('{} * {} = {}'.format(n,i,t))
    