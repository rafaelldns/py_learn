print('== CHALLENGE 42 ==')
l1 = float(input('Insert first line: '))
l2 = float(input('Insert second line: '))
l3 = float(input('Insert third line: '))

if l1 < l2+l3 and l2 < l3+l1 and l3 < l2+l1:
    print('These lines \033[0;32mCan\033[m form a triangle!')
    if l1 == l2 and l2 == l3:
        print('This triangle is equilateral!')
    elif l1 == l2 or l1 == l3 or l2 ==l3:
        print('This triangle is isosceles!')
    else:
        print('This triangle is scalene!') 
else:
    print('These lines \033[0;31mCan not\033[m form a triangle!')
    