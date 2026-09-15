print('== CHALLENGE 50 ==')
f = int(input('Enter the first term: '))
r = int(input('Enter the reason: '))

p = []
a = f

print('\nPrinting the first 10 terms of this progression:\n')
for i in range(0,10):
    p.append(str(a))
    a += r

res = ' -> '.join(p)

print(res)
