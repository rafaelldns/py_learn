print('{:^55}'.format('CHALLENGE 94') + '\n')

cad = dict()
temp = dict()
total = list()

while True:
    print(55*'=')
    temp['NAME'] = str(input('NAME: '))
    temp['SEX'] = str(input('SEX: [M/F] ')).upper()
    temp['AGE'] = int(input('AGE: '))

    cad = temp.copy()
    
    total.append(cad)
    temp.clear()

    op = 0

    while True:
        op = str(input('Want to continue? [Y/N] ')).upper()
        if op == 'Y' or op == 'N':
            break
        else:print('Invalid Value. Try Again!')
    if op == 'N':break

w_list = list()
sum_age = 0

for i in total:
    sum_age += i['AGE']
    if i['SEX'] == 'F':
            w_list.append(i['NAME'])

m_age = sum_age/len(total)

print(55*'='+f'\n- The group have {len(total)} persons\n' + 
f'- The medium age is {m_age} years\n- The list of womens cadastered is:', end="")
for k in w_list: print(f' {k}. ', end="")
print('\n- List of above average people: ')
for l in total: 
    if l['AGE'] > m_age: 
         print(f'NAME = {l["NAME"]}; SEX = {l["SEX"]}; AGE = {l["AGE"]}')
