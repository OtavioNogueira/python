p = float(input('Insira o valor do produto: '))

desconto = ((p*5)/100) 
p2 = p-desconto

print('O preço com desconto de 5 por cento aplicado é de R${}'.format(p2))