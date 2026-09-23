print('== CHALLENGE 15 ==')
km = float(input('Km traversed? '))
d = float(input('Days allocated? '))

pd = 60*d
pkm = 0.15*km

pt = pd+pkm

print("The Total price to pay is R${} ; For Km R${} ; For days R${}".format(pt,pkm,pd))
