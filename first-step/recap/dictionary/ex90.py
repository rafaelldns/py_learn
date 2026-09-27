print("{:^55}".format('CHALLENGE 90'))

dic = dict()

dic['Name'] = str(input('Name: '))
dic['Media'] = float(input('Media: '))
dic['Situation'] = str(input('Situation: '))

print(dic)

for i,j in dic.items():
    print(f'{i} is {j}')
    
