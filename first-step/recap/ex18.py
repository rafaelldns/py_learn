from math import cos, sin, tan, radians
print('== CHALLENGE 18 ==')
a = float(input('Insert an angle: '))
r = radians(a)

c = cos(r)
s = sin(r)
t = tan(r)

print('There Cosine: {:.2f}, Sine {:.2f}, Tangent {:.2f}'.format(c, s, t))
