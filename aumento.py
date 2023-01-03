from re import S


s = float(input('Insira o salário para acrescentar o aumento: '))

aumento = (s*15)/100
s2 = aumento+s 

print('O salário com aumento de 15 por cento será de R${}'.format(s2))