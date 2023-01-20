from random import randint
aux = 1

while aux != 0:
  pc = randint(0,10) 
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  user = int(input('Insira um valor: '))
  choice = str(input('Par ou Ímpar: ')).upper()
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

  soma = pc + user

  if choice == 'PAR':
    if soma % 2 == 0: 
      print(f'O computador jogou {pc}!')
      print('Deu par! Você venceu!!')
    else: 
      print(f'O computador jogou {pc}!')
      print('Deu ímpar! Você perdeu.')
      aux = 0
  elif choice == 'IMPAR':
    if soma % 2 == 0: 
      print(f'O computador jogou {pc}!')
      print('Deu par! Você perdeu.')
      aux = 0
    else: 
      print(f'O computador jogou {pc}!')
      print('Deu ímpar! Você venceu!!')
