n = 0.5
cont = 0
soma = 0
maior = 0
menor = 0

while n != 0:
  n = int(input('Insira um valor: '))
  maior = n
  menor = n
  if maior > n:
    maior = n
  elif menor < n:
    menor = n
  soma += n
  cont += 1

print(soma)
print('A média dos valores inseridos foi: {}'.format(soma/(cont-1)))
print(maior)
print(menor)