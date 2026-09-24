import re
print('{:^55}'.format('CHALLENGE 77'))

words = ('Trabalhar', 'Falar', 'Estudar',
        'Jogar', 'Treinar', 'Praticar',
        'Escola', 'Faculdade', 'Livro')

for i in range(0,len(words)):
    vow = re.findall(r'[a,e,i,o,u]', words[i], re.IGNORECASE)
    print(f'In the Word: {words[i].upper()} Have the vowels: {vow}')
