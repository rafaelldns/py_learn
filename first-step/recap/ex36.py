print('\033[m== CHALLENGE 36 ==')
h = float(input('Insert a house value: \033[0;32mR$'))
w = float(input('\033[mInsert your wage: \033[0;32mR$'))
y = float(input('\033[mInsert years for payment: \033[0;34m'))

i = (h/y)/12

if i > (w/100*30):
    print('''\033[m\033[0;31mLoan denied\033[m because the installments \
exceed 30 percent of your salary: \033[0;32mR${:.2f}\033[m'''.format(i))
else:
    print('''\033[0;32mLoan approved\033[m \
The installment amounts is: \033[0;32mR${:.2f}\033[m'''.format(i))
