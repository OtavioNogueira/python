aux = ''
midd = 0
masc = 0
femi20 = 0

while aux != 'N': 
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  idade = int(input('Insira sua idade: '))
  sexo = str(input('Insira seu sexo [M/F]: ')).upper().strip()

  print('PESSOA CADASTRADA!')
  
  if idade >= 18:
    midd += 1
  if sexo == 'M':
    masc += 1
  if idade < 20 and sexo == 'F':
    femi20 += 1
  
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

  aux = str(input('Deseja continuar? [S/N]: ')).upper().strip()
  if aux == 'N':
    aux = 'N'

print(f'Esse é o número de pessoas com mais de 18 anos: {midd}')
print(f'Esse é o número de homens cadastrados: {masc}')
print(f'Esse é o número de mulheres com menos de 20 anos: {femi20}')

