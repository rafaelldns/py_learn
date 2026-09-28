print('{:^55}'.format('CHALLENGE 92'))

cad = dict()

while True:
    cad['NAME'] = str(input("NAME: "))
    cad['BIRTH YEAR'] = int(input('YEAR OF BIRTH: '))
    cad['EMPLOYMENT RECORD BOOK'] = int(input('CODE E.R.B.: '))

    if cad['EMPLOYMENT RECORD BOOK'] != 0:
        cad['YEAR OF HIRING'] = int(input('YEAR OF HIRING: '))
        cad['WAGE'] = float(input('WAGE: '))

    cad['AGE'] = 2026 - cad['BIRTH YEAR']
    cad['RETIREMENT'] = 