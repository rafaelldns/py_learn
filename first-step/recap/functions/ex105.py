def notes(note, sit=False):
    '''
    -> Function for analyze the notes and situation
    note: list from def receives
    sit: situation of media notes to show
    return: return dictionary with the notes situation 
    '''

    cad = dict()

    cad['TOTAL'] = len(note)
    
    big = note[0]
    for i in note:
        if big < i:
            big = i
    cad['BIGGER'] = big
    
    smal = note[0]
    for i in note:
        if smal > i:
            smal = i
    cad['SMALLEST'] = smal
    
    media = (sum(note))/len(note)
    cad['MEDIA'] = media
    
    if sit == True:
        if cad['MEDIA'] > 7.4:
            cad['SITUATION'] = 'Good'
        elif cad['MEDIA'] >5.9:
            cad['SITUATION'] = 'Reasonable'
        else:
            cad['SITUATION'] = 'Bad'

    return cad


def receives(msg):
    '''
    -> Function for receives how many notes user wants
    msg: Select whats message ask for user
    return: return the list of notes user insert
    '''

    note = list()
    
    while True:
        nt = float(input(msg))
        note.append(nt)
        
        op = 0 
        
        while True:
            op = input('Want to Insert More: [Y/N] ').upper()
            if op == 'Y' or op == 'N': break
            else: print('Invalid Value! Try Again.')
        if op == 'N': break
    
    return note


print('{:^55}'.format('CHALLENGE 105')+'\n'+55*'=')
help(receives)
help(notes)
print(55*'=')

var = receives('Note: ')
res = notes(var, sit=True)
print(res)
