import math

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

h = math.sqrt((math.pow(co,2)) + (math.pow(ca,2)))

print('O valor da hipotenusa é: {:.1f}'.format(h))
