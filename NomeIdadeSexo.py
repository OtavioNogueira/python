name = []
age = []
sex = []

for i in range (1,5):
  print('=-='*10)
  nome = str(input('Insira seu nome: '))
  name.append(nome)
  idade = int(input('Insira sua idade: '))
  age.append(idade)
  sexo = int(input('1 - Para sexo feminino; 0 - Para sexo masculino'))
  sex.append(sexo)
  print('=-='*10)

soma = age[0] + age[1] + age[2] + age[3]
media = soma/4
print('A média de idade é: {}'.format(media))

print('=-='*10)

print('O homem mais velho se chama: '.format(max))

