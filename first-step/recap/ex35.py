print('== CHALLENGE 35 ==')
l1,l2,l3 = map(float, input('Enter a three lines: \n').split(21))

if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print('These lines can form a triangle!')
else:
    print('These line can not form a triangle!')
