import random 
from time import sleep

pc = random.choice(['Pedra', 'Papel', 'Tesoura'])

jogo = str(input('Qual sua jogada: '))

print('Computador jogou {}'.format(pc))

if jogo == 'Pedra' and pc == 'Pedra':
  print('Empate')
elif jogo == 'Pedra' and pc == 'Papel':
  print('O computador venceu!')
elif jogo == 'Pedra' and pc == 'Tesoura':
  print('Você venceu! ')

elif jogo == 'Papel' and pc == 'Pedra':
  print('Você venceu! ')
elif jogo == 'Papel' and pc == 'Papel':
  print('Empate!')
elif jogo == 'Papel' and pc == 'Tesoura':
  print('O computador venceu! ')

elif jogo == 'Tesoura' and pc == 'Pedra':
  print('Você perdeu!')
elif jogo == 'Tesoura' and pc == 'Papel':
  print('Você venceu!')
elif jogo == 'Tesoura' and pc == 'Tesoura':
  print('Empate! ')
