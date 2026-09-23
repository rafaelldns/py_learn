print('== CHALLENGE 59 ==')

n1 = float(input("\nInsert a first number: "))
n2 = float(input('Insert a second number: '))

op = 0

while op != 5:
    print('\n======= MENU =======')
    print('[1] SUM\n[2] MULTIPLY\n[3] BIGGER\n[4] NEW NUMBERS\n[5] EXIT')
    op = int(input('\nInsert a option:\n'))
    if op == 1:
        sum = n1+n2
        print('\nThe sum is: {}'.format(sum))
    if op == 2:
        mult = n1*n2
        print('\nThe multiplication is: {}'.format(mult))
    if op == 3:
        if n1 > n2:
            print('\nThe bigger is {}'.format(n1))
        else:
            print('\nThe bigger is {}'.format(n2))
    if op == 4:
        n1 = float(input('\nInsert the new first number: '))
        n2 = float(input('Insert the new second number: '))
print('Exiting the program...')
