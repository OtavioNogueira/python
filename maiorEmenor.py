n1 = int(input('Insira o 1° valor: '))
n2 = int(input('Insira o 2° valor: '))
n3 = int(input('Insira o 3° valor: '))

if n1 > n2 and n1 > n3:
  print('{} é o maior valor'.format(n1))
elif n2 > n3 and n2 > n1:
  print('{} é o maior valor'.format(n2))
elif n3 > n2 and n3 > n1:
  print('{} é o maior valor'.format(n3))

if n1 < n2 and n1 < n3:
  print('{} é o menor valor'.format(n1))
elif n2 < n3 and n2 < n1:
  print('{} é o menor valor'.format(n2))
elif n3 < n2 and n3 < n1:
  print('{} é o menor valor'.format(n3))