print('== CHALLENGE 22 ==')
name = input('Insert your full name: ')

print('UPPER: {}'.format(name.upper()))
print('LOWER: {}'.format(name.lower()))
print('LETTERS: {}'.format(len(name.replace(' ', ''))))
print('LETTERS FIRST NAME: {}'.format(len(name.split()[0])))
