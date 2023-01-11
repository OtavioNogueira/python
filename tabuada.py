print('| TABUADA ATÉ 10 |')
for a in range(1, 10):
    print('=-=' *6)
    for b in range(1, 11):
        print('| {:2} x {:2} = {:2}  |'.format(a, b, a*b))
print('=-=' *6)
for i in range(1, 10):
    print('|  10 x {:2} = {:2} |'.format(i, i*10))