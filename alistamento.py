from datetime import date
presente = date.today().year

ano = int(input('Em que ano você nasceu: '))
idade = presente - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, presente))

if idade == 18:
  print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18: 
  print('Você ainda não precisa se alistar, somente daqui {} ano(s)'.format(18-idade))
elif idade > 18: 
  print('Você deveria ter se alista há {} ano(s)'.format(idade-18))

