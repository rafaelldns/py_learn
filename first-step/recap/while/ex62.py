print('== CHALLENGE 62 ==')

first = int(input('Enter the first term: '))
reason = int(input('Enter the reason: '))
max = 0
pa = first
pro = []

while max <10 : 
        pro.append(str(pa))
        pa += reason
        max +=1

rpro = ' -> '.join(pro)
print('This 10 terms PA:\n{}'.format(rpro))

more = 1

while more != 0:
    more = int(input('How many more terms do you want(0 to exit)? '))
    tempmore = more
    pro2 = []
    while tempmore != 0:
        pro2.append(str(pa))
        pa += reason 
        tempmore -= 1
    rpro2 = ' -> '.join(pro2)
    print(rpro2)
