r1 = float(input('Insira o tamanho da 1º reta: '))
r2 = float(input('Insira o tamanho da 2º reta: '))
r3 = float(input('Insira o tamanho da 3º reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: 
  print('É possível formar um triângulo')
  if r1 == r2 and r2 == r3:
    print('Ele seria equilátero!')
  elif (r1 == r2 and r2 != r3) or (r1 == r3 and r3 != r2) or (r2 == r3 and r3 != r1):
    print('Ele seria isóceles!')
  elif r1 != r2 and r2 != r3 and r3 != r1: 
    print('Ele seria escaleno!')
else: 
  print('Não é possível formar um triângulo')

