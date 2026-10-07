dou = hal = inc = dec = 0

def calcs(n):
    dou = n*2 
    dec = n - (n/100*13)
    inc = (n/100*10) + n
    hal = n/2 
    gold(dou, hal, inc, dec)


def gold(d,h,i,de):
    print(f'Double: R${d:.2f}')
    print(f'Half: R${h:.2f}')
    print(f'Increase 10%: R${i:.2f}')
    print(f'Decrease 13%: R${de:.2f}')

