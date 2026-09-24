print('{:^55}'.format('CHALLENGE 83'))

text = str(input('Insert an expression: '))
ch = list(text)
par_list = []

for par in ch:
    if par == '(' or par == ')':
        par_list.append(par)

if len(par_list) % 2 == 0:
    print('This expression is valid!')
else: print("This expression is not valid!")
