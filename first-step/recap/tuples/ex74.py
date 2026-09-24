import random
print('{:^55}'.format(' CHALLENGE 74 '))

tuple = ()

for i in range (0,5):
    num = random.randrange(0,11)
    tuple = tuple + (num, )

print(f"The tuple: {tuple}")

big = tuple[0]
smal = tuple[0]

for bigger in tuple:
    if big < bigger:
        big = bigger

print(f'The bigger: {big}')

for smaller in tuple:
    if smal > smaller:
        smal = smaller

print(f'The smaller: {smal}')
