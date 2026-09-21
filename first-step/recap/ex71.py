print('== CHALLENGE 71 ==')

print('\n========= ATM =========\n')

notes_disp = [50,20,10,1]
banknotes = {}

value = int(input('Insert a value to withdraw: '))

for note in notes_disp:
    if value >= note:
        quantity = value // note
        banknotes[note] = quantity
        value = value % note

for note, quantity in banknotes.items():
    print(f'Quantity for notes ${note}: {quantity}')
    