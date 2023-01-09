import random 
from time import sleep 

numero = random.randint(0,5)

chute = int(input('Insira um valor entre 0 e 5: '))

print('Processando...')
sleep(3)

if chute == numero : 
  print('Você acertou!! O valor pensado foi {}'.format(chute))
else:
  print('Incorreto, pensei no valor {}'.format(numero))