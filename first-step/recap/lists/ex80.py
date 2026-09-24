print('{:^55}'.format('CHALLENGE 80\n'))

list = []
comp = 0

for i in range(0,5):
    num = float(input(55*'='+"\nInsert an number: "))
    if len(list) == 0:
        list.append(num)
        print('Added in the final of list!')
        comp = num
    elif comp <= num:
        list.insert(i, num)
        print(f'Added in the position {i} of the list')
        comp = num
    elif comp > num:
        for ind, val in enumerate(list): 
            if num < val:
                list.insert(ind, num)
                print(f'Added in the position {ind} of the list')
                comp = num
                break

print(55*'='+f'\nThe final list is: {list}')
