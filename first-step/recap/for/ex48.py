print('== CHALLENGE 48 ==')

s = 0
count = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        s +=c
        count +=1
print('Sum of the values: {}\
      \nQuantity of values: {}'.format(s,count))
