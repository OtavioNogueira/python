from random import randint

a = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10) )

print(a)
print(f'Esse é o maior valor gerado {max(a)}')
print(f'Esse é o menor valor gerado {min(a)}')