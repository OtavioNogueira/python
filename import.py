import math
import random

num = int(input('Insira um valor: '))
num1 = random.randint(1, 10)

raiz = math.sqrt(num)

print('O número selecionado de maneira aleatória foi: {}'.format(num1))
print('A raiz de {} é {:.1f}'.format(num, raiz))