print('== CHALLENGE 70 ==')

price_s = []
prod_more_thousand = 0
name_prod = []

while True: 
    print(25*'=-')
    name = str(input('Insert product name: '))
    price = float(input('Insert price: \033[0;32m$'))
    print("\033[m" + 25*'=-')

    name_prod.append(name)
    price_s.append(price)

    if price > 1000:
        prod_more_thousand +=1

    op = str(input('You want to add more(Y/N)? '))

    if op != 'Y':
        break

name_low_prod = name_prod[0]
price_low_prod = price_s[0]

for i in range(1, len(name_prod)):
    if price_low_prod > price_s[i]:
        name_low_prod = name_prod[i]
        price_low_prod = price_s[i]
    
price_sum = sum(price_s)

print('''
The total spend: ${:.2f}
Products worth more than a $1000.00: {} 
Name of the cheapest product: {}
'''.format(price_sum, prod_more_thousand, name_low_prod))
