print('== CHALLENGE 55 ==')

weight = []

for i in range(0,5):
    wei = float(input('Insert a {}° weight: '.format(i+1)))
    weight.append(wei)

larger = weight[0]
smaller = weight[0]

for num in weight:
    if num > larger:
        larger = num
    if num < smaller:
        smaller = num

print('The largest weight is: {}\
      \nThe smallest weight is: {}'.format(larger,smaller))
    