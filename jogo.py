
secreto= 'lasanha'
digitado= []
chances= 3

while True:
    if chances <= 0:
        print(f'voce perdeu, a palavra era {secreto}')
        break

    letra= input('Digite um letra: ')

    if len(letra) > 1:
        print('somente uma letra por vez!!')
        continue

    digitado.append(letra)

    if letra in secreto:
        print(f'a letra {letra} esta na palavra secreta!!')
    else:
        print('voce errou!')
        digitado.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario+= '*'

    if secreto_temporario == secreto:
        print(f'Nice, voce ganhou, a palavra era {secreto_temporario}')
        break
    else:
        print(f'a palavra esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

        print()
        print(f'voce ainda tem {chances} chances.')