n = 1
par = 0
impar = 0

while n != 0:
  n = int(input('Insira um valor: '))
  if n % 2 == 0:
    par += 1
  else: 
    impar += 1

print('{} números pares'.format(par-1))
print('{} números impares'.format(impar))

