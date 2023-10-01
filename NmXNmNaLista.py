a = []
X = 1
M = 1

while X != 0 and M != 0:
    X, M = map(int,input().split(" "))
    a.append(X*M)

if a and a[-1] == 0:
    a.pop()
    
for i in a:
    print(' '.join(map(str, [i])))
