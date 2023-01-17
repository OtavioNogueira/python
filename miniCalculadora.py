n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

aux = 0

while aux != 5:
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  print('[1] Somar')
  print('[2] Multiplicar')
  print('[3] Maior')
  print('[4] Novos valores')
  print('[5] Sair')
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  aux = int(input('Insira o que deseja fazer: '))
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

  if aux == 1:
    print('A soma dos valores inseridos é {}'.format(n1+n2))
  elif aux == 2:
    print('A multiplicação dos valores inseridos é {}'.format(n1*n2))
  elif aux == 3:
    print('Dos valores inseridos, o maior é {}'.format(max(n1,n2)))
  elif aux == 4:
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))