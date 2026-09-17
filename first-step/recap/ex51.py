print('== CHALLENGE 50 ==')
f = int(input('Enter the first term: '))
r = int(input('Enter the reason: '))
t = f + (10-1) * r

p = []
a = f

print('\nPrinting the first 10 terms of this progression:\n')
for i in range(f,t,r):
    p.append(str(a))
    a += r

res = ' -> '.join(p)

print(res)
