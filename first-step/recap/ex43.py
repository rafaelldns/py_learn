print('== CHALLENGE 43 ==')
w = float(input('Insert your weight: '))
h = float(input('Insert your height: '))

imc = w/(w*h)

print('IMC: {} ')
if imc < 18.5:
    print('Below 18.5! Underweight!')
elif imc < 25:
    print('Beetwen 18.5 and 25! Ideal Weight!')
elif imc < 30:
    print('Beetwen 25 and 30! Overweight!')
elif imc < 40:
    print('Beetwen 30 and 40! Obesity!')
else:
    print('Above 40! Morbid Obesity!')
