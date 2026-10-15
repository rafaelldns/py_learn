import menu, time
cadt = dict()


def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR: Insert a valid integer number!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mERROR: The user didnt enter anything!')
            return 0
        else: return n


