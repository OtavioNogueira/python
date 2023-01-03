l = float(input('Insira a largura da parede: '))
a = float(input('Insira a altura da parede: '))

area = l*a
tinta = area//2

print('A área da parede é {} metros quadrados'.format(area))
print('Para pintar a parede serão necessários {} baldes de tinta'.format(tinta+1))