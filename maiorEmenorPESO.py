lista = []

print('=-='*10)

for i in range (1,4):
  peso = float(input('Insira seu peso em Kg: '))
  lista.append(peso)

print('=-='*10)

for i in range(3):
  print('{}º pessoa - {} Kg'.format(i+1, lista[i]))

print('=-='*10)

print('O menor peso inserido foi: {} Kg'.format(min(lista)))
print('O maior peso inserido foi: {} Kg'.format(max(lista)))

print('=-='*10)