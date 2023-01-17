import random

num = random.randint(1,10)
num2 = -1
aux = 0

while num != num2: 
  num2 = int(input('Tente adivinhar um valor entre 1 e 10: ')) 
  print('Tente novamente!')
  aux += 1
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Parabéns, você acertou! O número escolhido foi {}'.format(num))
print('Esse foi o total de tentativas: {}'.format(aux))