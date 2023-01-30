aux = 'S'
list = []

while aux == 'S' and aux != 'N':
  print('=-=' * 11)
  num = (int(input('Insira um valor para a lista: ')))
  if num in list: 
    print('Valor já inserido! Tente outro')
  else:
    print('Valor inserido com sucesso! ')
    list.append(num)
  print('=-=' * 11)
  aux = str(input('Deseja continuar? [S/N] ')).upper()

print('=-=' * 11)
print(f'Lista inserida: {list}')
list.sort()
print(f'Ordem crescente: {list}')
print('=-=' * 11)