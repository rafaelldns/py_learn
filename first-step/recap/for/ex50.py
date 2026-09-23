print('== CHALLENGE 50 ==')

n = 0
for i in range(1,7):
    v = int(input('Insert a integer {}: '.format(i)))
    if v % 2 == 0:
        n += v
print(n)
