def is_palindrome(phrase):
    # remover espaços
    phrase = phrase.replace(" ", "")
    # inverter a frase
    phrase_reverse = phrase[::-1]
    # comparar frase original com frase invertida
    if phrase == phrase_reverse:
        print('É um palíndromo!')
    else:
         print('Não é um palíndromo!')

frase = str(input('Insira uma frase: '))
is_palindrome(frase)