nome = str(input('Insira o seu nome completo: '))

print(nome.upper())
print(nome.lower())

nomeSE = nome.replace(' ', '')
print('Seu nome tem {} letras'.format(len(nomeSE)))

nomePN = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomePN[0])))