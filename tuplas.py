lanche = ('Hambúrguer', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche: 
  print(f'Eu vou comer {comida}')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posição {pos}')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

a = (1, 2, 3)
b = (4, 5, 6)

c = b + a 

print(c)
print(c.count(2)) #conta quantas vezes aparece
print(c.index(6)) #mostra em qual posição ele está