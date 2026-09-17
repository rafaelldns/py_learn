print('== CHALLENGE 67 ==')

print('\n', end='')
print( 30*'=')
print('==== Multiplication table ====')

while True:
    print(30*'=')
    num =  int(input("\nInsert an number to see(<0 to stop): "))
    print(30*'=')
    if num < 0:
        print('\nExiting...\n')
        break
    else:
        for i in range(1,11):
            res = num * i
            print(f'{num} x {i} = {res}')
