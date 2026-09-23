print('== CHALLENGE 40 ==')
n1 = float(input('Insert first note: '))
n2 = float(input('Insert second note: '))

m = (n1+n2)/2

if m >= 7 : 
    print('Congratulations you passed! your average is:\
\033[0;32m{:.1f}\033[m'.format(m))
elif m < 5 :
    print('You reproved! your average is:\
\033[0;31m{:.1f}\033[m'.format(m))
else:
    print('You need to retake the exam! Your average is:\
\033[0;33m{:.1f}\033[m'.format(m))
    