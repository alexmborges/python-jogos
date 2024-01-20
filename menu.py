import forca
import guess


def menu():
    print('--------------------------')
    print('Menu de jogos')
    print('--------------------------')

    print('(1) Forca', '(2) Guess Game', sep='\n')

    jogo = int(input('\nQual jogo deseja jogar? '))

    if jogo == 1:
        print('Iniciando Forca...')
        forca.jogar()
    elif jogo == 2:
        print('Iniciando Guess Game...')
        guess.jogar()


if __name__ == '__main__':
    menu()
