print("== CHALLENGE 66 ==")

num_vet=[]
counter = 1

while True:
    num = int(input(f'\nInsert a {counter}º number(999 to stop): '))
    if num == 999:
        break
    else: 
        counter +=1
        num_vet.append(num)

res = sum(num_vet)

print(f'''\n
Were inserted {counter} numbers
The sum of these numbers is: {res}
\n''')
