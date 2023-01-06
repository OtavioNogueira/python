n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1+n2)/2

print('A sua média foi {}'.format(media))

if media >= 6:
  print('Aprovado')
else:
  print('Reprovado')