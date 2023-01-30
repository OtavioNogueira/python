list = []

for i in range (0, 5):
  list.append(int(input(f'Insira o {i+1}º valor: ')))

print(f'Esse foi o maior valor inserido: {max(list)}. Ele está na posição {list.index(max(list))}')
print(f'Esse foi o menor valor inserido: {min(list)}. Ele está na posição {list.index(min(list))}')
