
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
valor = int(input('Insira o valor: '))

ci = int(valor / 50)
ci2 = valor % 50 

vi = int(ci2/20)
vi2 = (ci2 % 20)

de = int((vi2) / 10)
de2 = (vi2 % 10)

um = int(de2 / 1)

print(f'Esse é o total de notas de R$50: {ci}')
print(f'Esse é o total de notas de R$20: {vi}')
print(f'Esse é o total de notas de R$10: {de}')
print(f'Esse é o total de notas de R$1: {um}')
