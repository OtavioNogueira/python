a = ('aureo', 'nuvem','amarelo', 'caminhar', 'entender', 'palavra')

for i in a:
    print(f'\nAs vogais da palavra "{i}" são: ',end = '' )
    for letra in i:
        if letra.lower() in 'aeiou': 
            print(letra, end = ' ')
  
