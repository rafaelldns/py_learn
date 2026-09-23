print('== CHALLENGE 34 ==')
w = float(input('Enter a wage: \033[0;32mR$'))

if w > 1250:
    nw = (w/100*10) + w
    print('\033[mThe new wage with \033[0;34m10 percent\033[m increase: \033[0;32mR${:.2f}\033[m'.format(nw))
else:
    nw = (w/100*15) + w
    print('\033[mThe new wage with \033[0;34m15 percent\033[m increase: \033[0;32mR${:.2f}\033[m'.format(nw))
