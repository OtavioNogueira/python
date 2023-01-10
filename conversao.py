n = int(input('Insira um valor inteiro: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-')
print('[1] - binário')
print('[2] - octal')
print('[3] - hexadecimal')
print('-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-')
base = int(input('Qual base de conversão deseja: '))

if base == 1:
  print('O valor {} covertido para binário fica {}.'.format(n, bin(n).replace('0b','')))
elif base == 2:
  print('O valor {} covertido para octal fica {}.'.format(n, oct(n).replace('0o','')))
elif base == 3:
  print('O valor {} covertido para hexadecimal fica {}.'.format(n, hex(n).replace('0x','')))

