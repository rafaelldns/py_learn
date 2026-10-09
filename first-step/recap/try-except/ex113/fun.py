def readInt(msg):
    n = 0
    while True:
        try:
            n = int(input(f'{msg}'))
        except Exception:
            print('\033[0;31mERROR: Insert a integer number valid!\033[m')
        else:
            break
    return n


def readFloat(msg):
    n = 0
    while True:
        try:
            n = float(input(f'{msg}'))
        except Exception:
            print('\033[0;31mERROR: Insert a real number valid!\033[m')
        else:
            break    
    return n

            