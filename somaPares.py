soma = 0

for i in range (1,7):
  num = int(input('Insira o {}° valor: '.format(i)))
  if num % 2 == 0:
    soma += num
print('A soma dos valores é {}'.format(soma))