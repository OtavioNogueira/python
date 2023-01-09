r1 = float(input('Insira o tamanho da 1º reta: '))
r2 = float(input('Insira o tamanho da 2º reta: '))
r3 = float(input('Insira o tamanho da 3º reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: 
  print('É possível formar um triângulo')
else: 
  print('Não é possível formar um triângulo')