n, s = map(int, input().split(" "))
extrato = []

for i in range(n):
    valor = int(input())
    s += valor
    extrato.append(s)
    
print(min(extrato))
