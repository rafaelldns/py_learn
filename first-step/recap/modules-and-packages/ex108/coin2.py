def double(n = 0):
    dou = n*2
    return dou


def half(n = 0):
    hal = n/2 
    return hal


def increase(n = 0):
    inc = (n/100*10) + n
    return inc


def decrease(n = 0):
    dec = n - (n/100*13)
    return dec


def gold(n = 0, gold = 'R$'):
    return f'{gold}{n:.2f}'

