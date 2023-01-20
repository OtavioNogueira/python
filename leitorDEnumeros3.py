n = 0
count = 0
soma = 0

while n != 999: 
  n = int(input('Insira um valor: '))
  soma += n
  count += 1

print(f'A soma dos valores inserido resulta em {soma}')
print(f'Esse é o total de números digitados: {count}')