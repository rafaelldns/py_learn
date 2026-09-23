print('{:^30}'.format('== CHALLENGE 71 =='))

print(30*'=')
print('{:^30}'.format('ATM'))
print(30*'=')

value = int(input('Insert a value to withdraw: '))

tot = value
note = 50
tot_note = 0

while True:
    if tot >= note:
        tot -= note
        tot_note +=1
    else:
        if tot_note > 0:
            print(f'Total notes of {note} is : {tot_note}')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        tot_note = 0
        if tot == 0:
            break


'''
notes_disp = [50,20,10,1]
banknotes = {}

value = int(input('Insert a value to withdraw: '))

for note in notes_disp:
    if value >= note:
        quantity = value // note
        banknotes[note] = quantity
        value = value % note

for note, quantity in banknotes.items():
    print(f'Quantity for notes ${note}: {quantity}')'''    

