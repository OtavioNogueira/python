cont = 0
n = 0
soma = 0

while n != 999:
  n = int(input('Insira um valor: '))
  soma += n 
  cont += 1
  
print('A soma total resulta em: {}'.format(soma-999))
print('Esse é o total de números digitados: {}'.format(cont-1))
