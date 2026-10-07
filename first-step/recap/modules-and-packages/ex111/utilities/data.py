def read_cash(msg):
    op = 0
    while True:
        op = input(f'{msg}: ').strip()
        if op.replace('.', '', 1).isnumeric() == True:
            return float(op)
        else:
            print(f'\033[0;31mERROR: "{op}" is a invalid value!\033[m')
