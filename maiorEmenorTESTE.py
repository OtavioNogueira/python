
cont = 0

while cont < 4:
  num = int(input('Insira um valor: '))
  cont += 1
  if cont == 1:
    menor = num
    maior = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
    
print(f'Esse é o maior valor {maior}')
print(f'Esse é o menor valor {menor}')