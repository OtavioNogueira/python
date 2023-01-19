n = 0
cont = 0
soma = 0
aux = ''
lista = []

while aux != 'N':
  n = int(input('Insira um valor: '))
  soma += n
  cont += 1
  lista.append(n)
  aux = str(input('Deseja continuar? [S/N] ')).upper()
  if aux == 'N':
    aux = 'N'

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('A soma de todos os valores resulta em: {}'.format(soma))
print('Essa foi a quantidade de números inseridos: {}'.format(cont))
print('A média dos valores inseridos foi: {}'.format(soma/(cont)))
print('O maior valor inserido foi: {}'.format(max(lista)))
print('O menor valor inserido foi: {}'.format(min(lista)))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')