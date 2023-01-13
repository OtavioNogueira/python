from datetime import date
presente = date.today().year 

aux = []
m18= 0
l18= 0

print('=-='*16)

for i in range (1,8):
  nasc = int(input('Insira seu ano de nascimento: '))
  aux.append(nasc)

print('=-='*16)

for i in range (7):
  idade = presente - aux[i]
  if idade >= 18:
    print('O ano de nascimento é {}. Logo, maior de idade!'.format(aux[i]))
    m18 += 1
  elif idade < 18: 
    print('O ano de nascimento é {}. Logo, menor de idade!'.format(aux[i])) 
    l18 += 1

print('=-='*16)

print('Esse é o número de pessoas com mais de 18 anos: {}'.format(m18))
print('Esse é o número de pessoas com menos de 18 anos: {}'.format(l18))
  

