print('{:^55}'.format('CHALLENGE 80\n'))

list = []
comp = 0

for i in range(0,5):
    num = float(input(55*'='+"\nInsert an number: "))
    if len(list) == 0:
        list.append(num)
        comp = num
    elif comp <= num:
        list.insert(i, num)
        comp = num
    elif comp > num:
        for ind, val in enumerate(list): 
            if num < val:
                list.insert(ind, num)
                comp = num
                break

print(55*'='+f'\nThe final list is: {list}')