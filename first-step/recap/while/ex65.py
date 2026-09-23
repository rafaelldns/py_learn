print('== CHALLENGE 65 ==')

op = 'Y'
x = 1
num_list = []

while op == 'Y':
    num = int(input('Insert {}º integer: '.format(x)))
    op = str(input('You want to continue(Y/N)?')).upper()
    x +=1
    num_list.append(num)

res_sum = sum(num_list)

x2 = len(num_list)
pos = 0
big = num_list[0]
smal = num_list[0]

for i in range(1, x2):
    if big < num_list[i]:
        big = num_list[i]
    if smal > num_list[i]:
        smal = num_list[i]

print('''
\nThe sum of all numbers is: {}
The biggest number is: {}
The smallest number is: {}
'''.format(res_sum,big,smal))
