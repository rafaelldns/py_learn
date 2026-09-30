print('{:^55}'.format('CHALLENGE 97'))

def write(msg):
    c = len(msg) + 4
    print(c*'-')
    print(f'  {msg}')
    print(c*'-')


write('Training')
write('Testing This on VSCode')
write('Complete')
