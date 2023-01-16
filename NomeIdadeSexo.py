somaidade = 0
media = 0
maioridadeH = 0
nomevelho = ''
idadeM = 0

for i in range (1,3):
  print('=-=-=-= {}º pessoa =-=-=-='.format(i))
  nome = str(input('Insira seu nome: '))
  
  idade = int(input('Insira sua idade: '))
  somaidade += idade 

  sexo = str(input('Insira seu sexo [M/F]: ')).strip()

  if i == 1 and sexo in 'Mm':
    maioridadeH = idade 
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridadeH:
    maioridadeH = idade
    nomevelho = nome
  if sexo in 'Ff' and idade > 20:
    idadeM += 1
  
  print('=-=-=-==-=-=-=-=-=-=-=-=-=')

media = somaidade/2
print('A média de idade é: {}'.format(media))

print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeH, nomevelho))

print('Esse é o número de mulheres com mais de 20 anos: {}'.format(idadeM))
print('=-=-=-==-=-=-=-=-=-=-=-=-=')


