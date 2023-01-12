n = int(input('Insira um valor para saber se é primo: '))

if n == 2 or n == 3:
  print('O valor {} é primo!'.format(n))
elif (n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n != 1): 
  print('O valor {} é primo!'.format(n))
else:
  print('O valor {} não é primo!'.format(n))