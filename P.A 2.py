t1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))

t2 = t1
i = 1
total = 0
mais = 11

while mais != 0:
  total += mais
  while i < total:
    print('{}'.format(t1))
    t1 += r 
    i += 1

  mais = int(input('Quantos termos a mais você deseja: '))
print('{} termos foram mostrados!'.format(total-1))
