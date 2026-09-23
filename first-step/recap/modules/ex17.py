from math import hypot
print('== CHALLENGE 17 ==')
ol = float(input('Insert a Opposite Leg: '))
oa = float(input('Insert a Adjacent Leg: '))

h = hypot(ol,oa)

print('The hypotenuse is: {} or {}'.format(h, hypot(ol,oa)))
