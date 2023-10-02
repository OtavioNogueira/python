n = int(input())
resultado = []

for i in range(n):
    joao = []
    maria = []
    for i in range (3):
        x, d = map(int, input().split(" "))
        joao.append(x*d)
        
    for i in range (3):
        x, d = map(int, input().split(" "))
        maria.append(x*d)

    if sum(joao) > sum(maria):
        resultado.append("JOAO")
    else:
        resultado.append("MARIA")
        
for i in resultado:
    print(i)
