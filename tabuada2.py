n = 1

while n > 0:
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  n = int(input('Deseja ver a tabuada de qual valor: '))
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  i = 0
  for i in range (11):
    if n < 1:
      n = 0
    else:
      print(f'| ↦  {n} X {i} = {n*i}')
      i += 1
  