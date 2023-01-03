print('TABUADA DE 0 A 9:')
for a in range(1, 10):
    print('--' *5)
    for b in range(1, 11):
        print('{:2} x {:2} = {:2}'.format(a, b, a*b))