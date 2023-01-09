sal = float(input('Insira o salário para calcular o reajuste: '))

aumento10 = (sal*10)/100
aumento15 = (sal*15)/100

if sal > 1250.00:
  print('O novo salário será de R${}'.format(aumento10+sal))
else:
  print('O novo salário será de R${}'.format(aumento15+sal))