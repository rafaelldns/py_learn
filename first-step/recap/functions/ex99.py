print('{:^55}'.format('CHALLENGE 99'))

def bigger(* num):
    aux = 0
    print('\n'+55*'='+'\nAnalyzing the values...')
    if len(num) > 0:
        for j in num:
            if aux < j:
                aux = j
        
            print(f"{j}, ", end='')
    print(f'Were informed {len(num)} in total')
    print(f'The biggest value informed is {aux}')

bigger(8, 7, 9, 5, 4, 3)
bigger(6, 2, 8)
bigger(1, 4)
bigger(2)
bigger()
