print('== CHALLENGE 72 ==')

nums = ('Zero', 'One', 'Two', 'Tree', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fiveteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')

while True:
    desired_num = int(input('Insert a number to see your external(0/20): '))
    if desired_num < 0 or desired_num > 20:
        print('Try Again')
    else:
        print(f'The desired number is: {nums[desired_num]}')
        break
