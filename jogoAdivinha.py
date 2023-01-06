import random 

numero = random.randint(0,5)

chute = int(input('Insira um valor entre 0 e 5: '))

if chute == numero : 
  print('Você acertou!!')
else:
  print('Incorreto')