print('== CHALLENGE 69 ==')

i = 1
count_f = 0
count_age = 0
count_m = 0


while True: 
    print(25*'=-')
    age = int(input(f'{i}º Age: '))
    sex = str(input(f'{i}º Sex(M/F):')).upper()
    print(25*'=-')
    if age > 17:
        count_age +=1
    if sex == 'M':
        count_m +=1
    if sex == 'F':
        if age < 20:
            count_f += 1
    op = str(input('Want to add more(Y/N): ')).upper()
    if op != 'Y':
        break
print(f'''
{count_age} More 18 years old!
{count_m} Mens registered!
{count_f} Womens under the age of 20!
''')
