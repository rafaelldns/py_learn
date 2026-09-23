print('== CHALLENGE 23 ==')
ns = input('Insert a number(0 - 9999): ')

d1 = [int(char) for char in str(ns)]
print('Unit: {}'.format(d1[3]))
print('Tens place: {}'.format(d1[2]))
print('Hundred: {}'.format(d1[1]))
print('Thousand: {}'.format(d1[0]))

nm = int(input('\nInsert another number(0 - 9999): '))
d2 = []

while nm > 0:
    d2.insert(0, nm % 10)
    nm = nm // 10

print('Unit: {}'.format(d2[3]))
print('Tens place: {}'.format(d2[2]))
print('Hundred: {}'.format(d2[1]))
print('Thousand: {}'.format(d2[0]))
