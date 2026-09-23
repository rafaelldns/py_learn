from random import shuffle
print('== CHALLENGE 20 ==')
n1 = input('Insert a first name: ')
n2 = input('Insert a second name: ')
n3 = input('Insert a third name: ')
n4 = input('Insert a fourth name: ')
names = [n1,n2,n3,n4]
shuffle(names)

print('The order is : {}'.format(names))
