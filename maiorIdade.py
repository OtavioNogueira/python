from datetime import date
presente = date.today().year 

aux = []

for i in range (1,3):
  nasc = int(input('Insira seu ano de nascimento: '))
  aux.append(nasc)

for i in range (2):
  idade = presente - aux[i]
  if idade >= 18:
    print('O ano de nascimento é {}. Logo, maior de idade!'.format(aux[i]))
  elif idade < 18: 
    print('O ano de nascimento é {}. Logo, menor de idade!'.format(aux[i])) 

  

