from math import factorial

n = int(input('Insira um valor: '))
c = n
f = 1

while c > 0:
  print('{}'.format(c),end = '')
  print(' x ' if c > 1 else ' = ',end = '')
  f *= c
  c -= 1

print('O fatorial desse valor resulta em: {}'.format(f))