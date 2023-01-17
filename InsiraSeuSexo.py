n = 2

while n != 0:
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  mf = str(input('Insira seu sexo [M/F]: '))
  if mf == 'M' or mf == 'F':
    print('Salvo!')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    n = 0
  else:
    print('Valor não aceito!')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    n = int(input('Digite 1 para inserir novemente: '))
  