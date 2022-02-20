
from time import sleep
secreto = 'PERFUME'
digitadas = []
chances = 2

print('##JOGO DA ADIVINHAÇÃO##')
print("-=-" *20)
print('VOCÊ TEM DUAS TENTATIVAS!')
print("-=-" *20)
print('Tenha um bom Jogo!!')
print("-=-" *20)
print('CARREGANDO')
print("-=-" * 20)

while True:
    if chances <= 0:
        print('VOCÊ PERDEU!!!')
        break

    letra = input('Digite uma letra: ')
    print('CARREGANDO')
    print("-=-" *20)
    sleep(2)
    if len(letra) > 1:
        print('Ahhh, isso não vale, digite apenas uma letra!')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Uhull, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFzZZ: a letra "{letra}" NÂO EXISTE na "palavra secreta".')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
           secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'QUE LEGAL! VOCÊ GANHOU... A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chance. ')
    print("-=-" *20)
    print()

print("-=-" * 20)
print('##################### FIM ####################')
print("-=-" * 20)













