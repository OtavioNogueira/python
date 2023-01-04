dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos Km foram percorridos: '))

preco = (dias*60)+(km*0.15)

print('O valor do aluguel será de R${:.2f}'.format(preco))