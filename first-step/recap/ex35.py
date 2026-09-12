print('== CHALLENGE 35 ==')
l1,l2,l3 = map(float, input('Enter a three lines: \n').split())

if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print('These lines \033[0;32mcan\033[m form a triangle!')
else:
    print('These line \033[0;31mcan not\033[m form a triangle!')
