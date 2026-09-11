print('== CHALLENGE 34 ==')
w = float(input('Enter a wage: R$'))

if w > 1250:
    nw = (w/100*10) + w
    print('The new wage with 10 percent increase: R${:.2f}'.format(nw))
else:
    nw = (w/100*15) + w
    print('The new wage with 15 percent increase: R${:.2f}'.format(nw))
