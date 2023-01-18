a = 0
b = 1
aux = 0 

tam = int(input('Quantos valores deseja ver da sequência de Fibonacci? '))

while aux < tam+1:
  print('{} - '.format(a), end = '')
  x = a
  a = b
  b = b + x
  aux += 1
print('FIM',end = '')