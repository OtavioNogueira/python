from datetime import date 
presente = date.today().year 

ano = int(input('Informe seu ano de nascimento: '))

idade = presente - ano

if idade <= 9: 
  print('ATLETA MIRIM')
elif 10 <= idade <= 14:
  print('ATLETA INFANTIL')
elif 15 <= idade <= 19:
  print('ATLETA JUNIOR')
elif 20 <= idade <= 25: 
  print('ATLETA SÊNIOR')
elif 26 <= idade: 
  print('ATLETA MASTER')