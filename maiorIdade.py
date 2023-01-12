from datetime import date
presente = date.today().year 

aux = []
aux2 = 0
for i in range (1,3):
  nasc = int(input('Insira seu ano de nascimento: '))
  aux.append(nasc)

for i in range (1,3):
  print('{}'.format(aux[aux2]))
  if presente - nasc > 18:
    print('Maior de idade!')
  elif presente - nasc < 18: 
    print('Menor de idade! ')
  aux2 += 1


  

