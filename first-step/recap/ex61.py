print('== CHALLENGE 61 ==')

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
