a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
  num = int(input('Insira um valor de 0 a 20: '))
  if 0 <= num < 21:
    print(f'Você digitou o número {a[num]}')
    break
  print('Tente novamente. ', end='')

print('=-=' * 11)