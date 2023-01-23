
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
valor = int(input('Insira o valor: '))

ci = round(valor/50)
ci2 = ci * 50

vi = round((valor - ci2)/20)
vi2 = vi * 20

de = round(valor - (ci2 + vi2)/10)
de2 = de * 10

um = round(valor - (ci2 + vi2 + de2)/1)

print(f'Esse é o total de notas de R$50: {ci}')
print(f'Esse é o total de notas de R$20: {vi}')
print(f'Esse é o total de notas de R$10: {de}')
print(f'Esse é o total de notas de R$1: {um}')
