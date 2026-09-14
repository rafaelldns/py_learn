print('== CHALLENGE 44 ==')
p = float(input('Insert the product price: \033[0;32mR$'))
pay = str(input('\033[mInsert payment method(Cash/Check/Card): '))

pay = pay.upper()

if 'CASH' in pay or 'CHECK' in pay:
    p = p-(p/100*10)
    print('This Method have 10 percent of discount!\
          \nThe new price is \033[0;32mR${}\033[m'.format(p))
elif 'CARD' in pay:
    met = str(input('Credit or debit? '))
    met = met.upper()
    if 'DEBIT' in met:
        p = p-(p/100*5)
        print('This method have 5 percent of discount!\
              \nThe new price is \033[0;32mR${}\033[m'.format(p))
    elif 'CREDIT' in met:
        x = int(input('Enter the number off installments: '))
        if x == 1 or x == 2:
            print('This method stay with normal price:\
                   \n\033[0;32mR${}\033[m'.format(p))
        elif x > 2:
            p = p+(p/100*20)
            print('This method have 20 percent interest!\
                  \nThe new price is \033[0;32mR${}\033[m'.format(p))
        else:
            print('Invalid Value! Try Again!')
    else:
        print('Invalid Value! Try Again!')
else:
    print('Invalid Value! Try Again!')
