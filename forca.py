import random


# Função principal:
def jogar():
    cabecalho()
    palavra_secreta = gerar_palavra()
    letras_corretas = gerar_letras_corretas(palavra_secreta)
    print(letras_corretas)

    enforcou = False
    acertou = False
    letras_erradas = 0

    # while True
    while not enforcou and not acertou:
        chute_letra = chuta()

        if chute_letra in palavra_secreta:
            chute_correto(chute_letra, letras_corretas, palavra_secreta)
        else:
            letras_erradas = letras_erradas + 1

        enforcou = letras_erradas == len(palavra_secreta)  # ou o número de letras da palavra_secreta
        acertou = '_' not in letras_corretas
        print(letras_corretas)

    if acertou:
        print(f'Parabéns! A palavra secreta era {palavra_secreta} e você acertou!')
    else:
        print(f'Você perdeu! A palavra secreta era {palavra_secreta}\n')
        print('Você foi enforcado...')


# Definindo as funções do jogo:
def cabecalho():
    print('--------------------------')
    print('Bem-vindo ao jogo da Forca')
    print('--------------------------\n')


def gerar_palavra():
    arquivo = open('dados.txt', 'r')
    banco_de_palavras = []
    for linha in arquivo:
        linha = linha.strip()  # Para remover os espaços
        banco_de_palavras.append(linha)
    arquivo.close()

    aleatorizar = random.randrange(0, len(banco_de_palavras))
    palavra_secreta = banco_de_palavras[aleatorizar].upper()
    return palavra_secreta  # O return é para a palavra_secreta poder retornar fora dessa função


def chuta():
    chute_letra = input('Digite uma letra: ').upper().strip()
    return chute_letra


def chute_correto(chute_letra, letras_corretas, palavra_secreta):
    index = 0  # poderia ser usada a palavra 'posição' ao invés de 'index'
    for letra in palavra_secreta:  # Sendo letra uma variável arbitrária
        if chute_letra == letra:
            letras_corretas[index] = letra
        index = index + 1


def gerar_letras_corretas(palavra):
    return ['_' for letra in palavra]  # Sendo letra uma variável arbitrária


if __name__ == '__main__':
    jogar()
