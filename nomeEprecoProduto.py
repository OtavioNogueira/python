aux = ''
total = 0
mil = 0
barato = ''
baratoRS = 0
cont = 0

while cont != -1:
  while aux != 'N':
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    cont += 1 

    total += preco

    if preco > 1000:
      mil += 1

    if cont == 1:
      barato = nome
      baratoRS = preco
    elif preco < baratoRS:
      barato = nome
      baratoRS = preco
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    aux = str(input('Deseja continuar? [S/N]: ')).upper()

  print(f'O total gasto na compra foi R${total}')
  print(f'Esse é o número de produtos que custam mais de mil reais: {mil}')
  print(f'Esse é o produto mais barato: {barato}')
  cont = 0
  break 
  
  

