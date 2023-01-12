soma = 0

for i in range(1,501):
  if i % 3 == 0 and i % 2 != 0:
    print('{}'.format(i))
    soma += i
print('{}'.format(soma))