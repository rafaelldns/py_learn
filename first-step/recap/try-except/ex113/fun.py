def readInt(msg):
    n = 0
    while True:
        try:
            n = input(msg)
        except n.isdigit() == True:
            print('\033[0;31mERROR: Insert a integer number valid!\033[m')
        else:
            break
    return n


def readFloat(msg):
    n = 0
    while True:
        try:
            n = input(msg)
        except n.isnumeric() == True:
            print('\033[0;31mERROR: Insert a real number valid!\033[m')
        else:
            break    
    return n

            