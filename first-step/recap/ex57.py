print('== CHALLENGE 57 ==')

print('[To exit loop insert 0]')
counter = 1

while counter != 0:
    op = str(input('Insert your sex: ')).upper()
    if op == 'M' or op == 'F':
        counter -=1
    else:
        print('Invalid value! Try again!')
print('Sucess!')
