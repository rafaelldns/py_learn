def double(n, form=False):
    d = n*2
    if form == True:
        return gold(d)
    else:
        return d


def half(n, form=False):
    h = n/2
    if form == True: return gold(h)
    else: return h


def increase(n, p, form=False):
    i = (n/100*p) + n
    if form == True: return gold(i)
    else: return i


def decrease(n, p, form=False):
    de = n - (n/100*p)
    if form == True: return gold(de)
    else: return de


def gold(n = 0, gol='R$'):
    return f'{gol}{n:.2f}'

