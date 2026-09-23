print('== CHALLENGE 37 ==')
n = int(input('Insert a integer: '))
o = int(input('''Choose the conversion base:
1 - Binary
2 - Oc
3 - Hexadecimal
: '''))

if o == 1:
    b = bin(n)
    bc = f"{n:b}"
    print(f'This integer in Binary: {bc}')
elif o == 2:
    oc = oct(n)
    occ = f"{n:o}"
    print(f'This integer in Oc: {occ}')
elif o == 3:
    h = hex(n)
    hc = f"{n:X}"
    print(f'this integer in Hexadecimal: {hc}')
else:
    print('Invalid Value! Try Again...')
