print('{:^55}'.format('CHALLENGE 89'))

total = []
students = []
note_temp = []

while True:
    print(55*'=')
    students.append((str(input('Name: '))))
    note_temp.append(float(input('Note 1: ')))
    note_temp.append(float(input('Note 2: ')))
    students.append(note_temp[:])
    total.append(students[:])
    note_temp.clear()
    students.clear()
    op = 0

    while True:
        op = str(input('Want to continue? [Y/N] ')).upper()
        if op == 'Y' or op == 'N':break
        else:print('Invalid Value. Try Again!')
    if op == 'N': break

print(f'{"CODE":<4} {"NAME":<12} {"MEDIA":>12}')

med = 0
print(55*'=')
for i, j in enumerate(total):
    temp = j[1]
    med = (sum(temp))/2
    print(f'{i:<4} {j[0]:<12} {med:>12}')

while True:
    print(55*'=')
    op = int(input('Show grades for which student?[999 to STOP] '))
    if op == 999:break
    else:
        print(f'Notes of {total[op][0]} are: {total[op][1]}')
            