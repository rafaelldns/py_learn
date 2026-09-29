print('{:^55}'.format('CHALLENGE 92'))

cad = dict()

cad['NAME'] = str(input("NAME: "))
yb = int(input('YEAR OF BIRTH: '))
cad['AGE'] = 2026 - yb
cad['EMPLOYMENT RECORD BOOK'] = int(input('CODE E.R.B.: '))

if cad['EMPLOYMENT RECORD BOOK'] != 0:
    cad['YEAR OF HIRING'] = int(input('YEAR OF HIRING: '))
    cad['WAGE'] = float(input('WAGE: '))
    yh = 2026 - cad['YEAR OF HIRING']
    cad['RETIREMENT'] = (35 - yh) + cad['AGE']

print(55*'=')
print(cad)

for i, j in cad.items():
    print(f'{i} = {j}')
