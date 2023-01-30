a = ('Pão', 2.00, 'Agua', 3.00, 'Biscoito', 4.00, 'Carne', 5.00, 'Refrigerante', 6.00,'Leite', 7.00)
i = 0
n = 0

print('=-=' * 13)
print('          LISTAGEM DE PREÇOS')
print('=-=' * 13)

while i < (len(a)/2):
  print(f'{a[n]:.<31}R${a[n+1]:>5.2f}')
  i += 1
  n += 2

print('=-=' * 13)