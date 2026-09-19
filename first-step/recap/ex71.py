print('== CHALLENGE 71 ==')

print('\n======= ATM =======\n')

value = int(input('Insert a value to withdraw: '))

rest_value = 0

while True:
    if value > 50:
        fifht_note = value // 50
        rest_value = value % 50
        if rest_value > 20:
            twenty_note = rest_value // 20
            rest_value = rest_value % 20 
            if rest_value > 10:
                ten_note = rest_value // 10
                rest_value = rest_value % 10
                if rest_value > 1:
                    one_note = rest_value//1
                    break
                else:
                    break
            elif rest_value > 1:
                one_note = rest_value//1
                break
            else:
                break
        elif rest_value > 10:
            ten_note = rest_value // 10
            rest_value = rest_value % 10
            if rest_value > 1:
                one_note = rest_value//1
                break
            else:
                break
        elif rest_value > 1:     
            one_note = rest_value//1
            break
        else:
            break
    elif value > 20:
        twenty_note = value // 20
        rest_value = value % 20
        if rest_value > 10:
            ten_note = rest_value //10
            rest_value = rest_value % 10
            if rest_value > 1:
                one_note = rest_value//1
                break
            else:
                break
        elif rest_value > 1:
            one_note = rest_value//1
            break
        else:
            break
    elif value > 10:
        ten_note = value //10
        rest_value = value % 10
        if rest_value > 1:
            one_note = rest_value//1
            break
        else:
            break
    elif value > 1:
        one_note = value//1
        break
    else:
        break

print(f'''
=== Banknotes to be printed ===
notes -> $50 : {fifht_note}
notes -> $20 : {twenty_note}
notes -> $10 : {ten_note}
notes -> $1 : {one_note}
''')