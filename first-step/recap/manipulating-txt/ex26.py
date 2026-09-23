print('== CHALLENGE 26 ==')
f = input('Insert a phrase: ')

f = f.upper()
print('(A) appearances: {}'.format(f.count('A')))
print('(A) first appearance: {}'.format(f.find('A')))
print('(A) last appearance: {}'.format(f.rfind('A')))
