nove = 0
par = 0

print('=-=' * 12)
w = int(input('Insira um valor: '))
x = int(input('Insira um valor: '))
y = int(input('Insira um valor: '))
z = int(input('Insira um valor: '))
print('=-=' * 12)
a = (w, x, y, z)

for i in a: 
  if i % 2 == 0:
    par += 1
if w % 2 == 0 or x % 2 == 0 or y % 2 == 0 or z % 2 == 0:
  print(f'Quantidade de números pares: {par}')
else:
  print('Não foram inseridos números pares!')

if w != 9 and x != 9 and y != 9 and z != 9:
  print('O valor 9 não foi digitado nenhuma vez!')
else:
  print(f'O valor 9 aparece {a.count(9)} vez(es)')

if w != 3 and x != 3 and y != 3 and z != 3:
  print('O valor 3 não foi digitado nenhuma vez!')
else: 
  print(f'O valor "3" aparece na posiçao {a.index(3)+1}')


