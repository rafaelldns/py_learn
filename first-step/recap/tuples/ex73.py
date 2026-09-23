print('{:=^55}'.format(' CHALLENGE 73 '))

bra = ('Flamengo', 'Palmeiras', 'AthleticoPR', 'Fluminense', 'Bahia',
'Cruzeiro', 'AtleticoMG', 'Santos', 'Coritiba', 'Bragantino',
'Sao Paulo', 'Botafogo', 'Vitoria', 'Corinthians', 'Mirassol',
'Vasco da Gama', 'Gremio', 'Internacional', 'Remo', 'Chapecoense')

print("{:^50}".format('Tabela do Brasileirão(23/09)'))

for pos in range(0, len(bra)):
    print(f'{pos+1} - {bra[pos]}')

print(55*'=' + '\n{:^55}'.format('5 Primeiros Colocados: '))

for pos in range(0, 5):
    print(f'{pos+1} - {bra[pos]}')

print(55*'=' + '\n{:^55}'.format('O Z4:'))

for pos in range (16, 20):
    print(f'{pos+1} - {bra[pos]}')

print(55*'=' + '{:^55}'.format('Times em ordem alfabética: '))

abra = sorted(bra)
for pos in range(0, len(bra)):
    print(f'{abra[pos]}')

print(55*'=' + '{:^55}'.format('Posição Chapecoense:'))
print(f'20 - {bra[19]}')