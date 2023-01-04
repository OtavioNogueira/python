import random 

a1 = input('Insira o nome do primeiro aluno: ')
a2 = input('Insira o nome do segundo aluno: ')
a3 = input('Insira o nome do terceiro aluno: ')
a4 = input('Insira o nome do quarto aluno: ')

nomes = [a1, a2, a3, a4]
escolha = random.choice(nomes)
random.shuffle(nomes)

print('O aluno escolhido para a primeira tarefa foi: {}'.format(escolha))
print('=========================================================')
print('A ordem para apresentar o trabalho será: {}'.format(nomes))