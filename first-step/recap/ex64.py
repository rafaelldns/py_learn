print('== CHALLENGE 64 ==')

n_stop = 0
counter = 0
sum_n = 0
nums = []

print('\n[To stop insert 999]\n')

while n_stop != 999:
    n = int(input('Insert a number: '))
    if n != 999: 
        n_stop = n
        nums.append(n)
        counter += 1
    else: 
        n_stop = n
    
sum_n = sum(nums)
print('The quantity of numbers inserted {}\nThe sum of numbers: {}'.format(counter, sum_n))
