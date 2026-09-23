print('== CHALLENGE 60 ==')

n = int(input('Insert a number for factorial: '))
print('{}!'.format(n))

var = []

for i in range(n, 0, -1):
    var.append(str(i))

rvar = ' x '.join(var)
print(rvar)

fact = n

while n != 1:
    fact *= (n-1)
    n -= 1

print('The factorial is: {}'.format(fact))
