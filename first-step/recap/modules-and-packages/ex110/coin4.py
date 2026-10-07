def resume(n, i, d):
    s = (55*'='+'\n'+ '{:^55}'.format('RESUME') 
    + '\n' + 55 *'='
    + f'\nAnalyzed price:   {gold(n)}'
    + f'\nDoubled price:    {double(n, True)}'
    + f'\nHalfed price:     {half(n, True)}'
    + f'\n80% increased:    {increase(n, i, True)}'
    + f'\n35% decreased:    {decrease(n, d, True)}'
    + '\n'+ 55*'=')
    return print(s)

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

