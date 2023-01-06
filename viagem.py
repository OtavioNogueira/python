dis = float(input('Qual a distância em Km da viagem? '))

if dis <= 200:
  preco1 = 0.5 * dis
  print('A passagem custará R${}'.format(preco1))
else:
  preco2 = 0.45 * dis
  print('A passagem custará R${}'.format(preco2))
