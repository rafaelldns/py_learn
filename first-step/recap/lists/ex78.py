print('{:^55}'.format('CHALLENGE 78\n'))

list = []

for i in range(0,5):
    list.append(int(input(f'Insert a {i+1}º number: ')))

bigger = list[0]
smaller = list[0]
ind_b = 0
ind_s = 0

for ind, nums in enumerate(list):
    if bigger < nums:
        bigger = nums
        ind_b = ind
    elif smaller > nums:
        smaller = nums
        ind_s = ind

print(55*'='+f'\nThe list inserted is:\n{list}')
print(f'The biggest value: {bigger} in index: {ind_b}')
print(f'The smallest value: {smaller} in index: {ind_s}')
