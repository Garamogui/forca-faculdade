'''
Crie um jogo interativo da forca em Python.
O programa deve escolher uma palavra aleatória de um dicionário.
O jogador deve tentar adivinhar a palavra letra por letra.
A cada letra errada, uma parte do boneco da forca é desenhada.
O jogador vence se adivinhar a palavra antes que o boneco seja completado.
'''

import random


def escolher_palavra():
    with open('words.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
        return random.choice(palavras).upper()


def jogar(palavra):
    boneco = [
        """
        --------
        |      |
        |      O
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
    ]


    letras_erradas = []
    letras_corretas = []
    palavra_secreta = []
    for letra in palavra:
        if letra == ' ':
            palavra_secreta.append(' ')
        else:
            palavra_secreta.append('_')

    enforcou = False
    acertou = False
    erros = 0
    print(boneco[erros])
    print(' '.join(palavra_secreta))

    while not enforcou and not acertou:
        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if chute in letras_erradas or chute in letras_corretas:
            print('Você já tentou esta letra!')
            continue

        if chute in palavra:
            letras_corretas.append(chute)
            index = 0
            for letra in palavra:
                if letra == chute:
                    palavra_secreta[index] = letra
                index += 1
        else:
            letras_erradas.append(chute)
            erros += 1
            print(boneco[erros])

        enforcou = erros == len(boneco) - 1
        acertou = '_' not in palavra_secreta
        print(' '.join(palavra_secreta))

    if acertou:
        print('Parabéns! Você acertou a palavra secreta!')
    else:
        print(f'Você perdeu! A palavra secreta era {palavra}.')

    print('Fim do jogo!')


if __name__ == "__main__":
    palavra = escolher_palavra()
    jogar(palavra)
