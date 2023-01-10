n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1+n2)/2

print('A sua média foi {}'.format(media))

if media < 5:
  print('Reprovado')
elif media >= 5 and media < 7:
  print('Recuperação')
else:
  print('Aprovado')