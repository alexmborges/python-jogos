import random


def jogar():
    print('--------------------------')
    print('Bem-vindo(a) jogo do número secreto')
    print('--------------------------')
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Esses serão os níveis de dificuldade:')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Selecione o nível de dificuldade:'))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute = input('Digite o seu palpite entre 1 e 100: ')
        print('Você chutou o número', chute)
        chute = int(chute)

        if chute < 1 or chute > 100:
            print('Número inválido!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Parabéns! Você acertou o número secreto. Sua pontuação foi de {} pontos'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! O número secreto é menor')
            elif menor:
                print('Você errou! O número secreto é maior')
            pontos_perdidos = abs(numero_secreto - chute)  # Onde abs são números absolutos
            pontos = pontos - pontos_perdidos

    print('Geme Over')


if __name__ == '__main__':
    jogar()