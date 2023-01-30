valores = []
num = [6, 9, 2, 8, 5, 4, 12, 1]

for cont in range(0, 5):
  valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

valores2 = valores[:] # maneira de criar uma cópia 


num[0] = 0.5 # define que a posição 0 será 0.5
num.append(3) #adiciona esse valor na lista, no fim
print(num)
num.sort() # ordena os valores em forma crescente
print(num)
num.sort(reverse=True) #ordena os valores de maneira descrescente
print(num)
print(f'Essa lista tem {len(num)} elemento(s)')
num.insert(0, 7) # insere o valor "7" na posição "0"
print(num)
print(f'Agora essa lista tem {len(num)} elemento(s)') 
num.pop() #excluirá o último valor da lista, no caso 0.5
print(num)
num.remove(12) #removerá o valor 12
