secreto = 'merda'
digitadas = []
chances = 6

while True:

    if chances == 0:
        print(f'voce perdeu, a palavra secreta era "{secreto}"')
        break
    letra = input('Digite uma letra: ')

    if len(letra)>1:
        
        letra = input('digite uma letra: ')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f' a letra "{letra}" está na palavra secreta.')

    else:
        print(f'a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()


    print(digitadas)

    secreto_temporario = ''
    for c in secreto:
        if c in digitadas:
            secreto_temporario+= c

        else:
            secreto_temporario+='#'

    
    print(secreto_temporario)
    if secreto_temporario == secreto:
        print('parabens voce venceuuu')
        break

    if letra not in secreto:
        chances -=1

    print(f'voce ainda tem {chances} chance(s)')

    


    