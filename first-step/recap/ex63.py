print('== CHALLENGE 63 ==')

n = int(input('How many terms you want to show? '))
t1 = 0
t2 = 1

if n != 0:
    if n == 1:
        print(t1)
    elif n >= 2:
        print(f'{t1} -> {t2}', end="")

    cont = 3

    while cont <= n:
        t3 = t1+t2
        print(f' -> {t3}', end="")
        t1 = t2
        t2 = t3
        cont +=1
