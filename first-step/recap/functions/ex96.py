print('{:^55}'.format('CHALLENGE 96'))

print('\n'+55*'-'+'\n{:^55}'.format('LAND CONTROL')+'\n'+55*'-')

def area(b, c):
    a = (b*c)
    print(f'\nThe area of the land with width {b}m and lenght {c}m is: {a:.1f}m²')


wid = float(input('\nWidht(m): '))
le = float(input('Lenght(m): '))

area(wid, le)
