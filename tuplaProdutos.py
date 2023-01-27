a = ('Pão', 2.00, 'Agua', 3.00, 'Biscoito', 4.00, 'Carne', 5.00, 'Refrigerante', 6.00)
i = 0
n = 0

print('=-=' * 13)
print('          LISTAGEM DE PREÇOS')
print('=-=' * 13)

while i < (len(a)/2):
  print(f'{a[n]} ......................R${a[n+1]}')
  i += 1
  n += 2

print('=-=' * 13)