print('== CHALLENGE 53 ==')
w = str(input('Insert a frase: ')).upper().replace(" ","")

reverse = w[::-1]
print(reverse)
print(w)

if reverse == w:
    print('Its a Palindrome!')
else:
    print('Itsnt a Palindrome!')
