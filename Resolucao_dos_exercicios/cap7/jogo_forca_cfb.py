import os
import random
from colorama import Fore, Back, Style

# Varíaveis Globais

jogar_novamente = 's'
jogadas = 0
quem_joga = 1
maxjogadas = 9
vit = 'n'
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# função de impressão


def tela():
    global velha
    global jogadas
    print('    0   1   2')
    print(f'0:  {velha[0][0]} |  {velha[0][1]} |  {velha[0][2]}')
    print('   -----------')
    print(f'1:  {velha[1][0]} |  {velha[1][1]} |  {velha[1][2]}')
    print('   -----------')
    print(f'2:  {velha[2][0]} |  {velha[2][1]} |  {velha[2][2]}')
    print(f'Jogadas:{Fore.GREEN} {jogadas} {Fore.RESET}')

def player1():
    global jogadas
    global quem_joga
    global vit
    global maxjogadas
    if quem_joga == 1 and jogadas < maxjogadas:
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna..: '))
            while velha[l][c] != ' ':
                l = int(input('Linha..: '))
                c = int(input('Coluna..: '))
            velha[l][c] = 'X'
            quem_joga = 2
            jogadas += 1
        except:
            print('Jogada Ínvalida')


def player2():
    global jogadas
    global quem_joga
    global maxjogadas
    if quem_joga == 2 and jogadas < maxjogadas:
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna..: '))
            while velha[l][c] != ' ':
                l = int(input('Linha..: '))
                c = int(input('Coluna..: '))
            velha[l][c] = 'O'
            quem_joga = 1
            jogadas += 1
        except:
            print('Linha e/ou coluna Ínvalida')
            os.system('pause')


def cpu():
    global jogadas
    global quem_joga
    global vit
    global maxjogadas
    if quem_joga == 2 and jogadas < maxjogadas:
        l = random.randint(0, 2)
        c = random.randint(0, 2)
        while velha[l][c] != ' ':
            l = random.randint(0, 2)
            c = random.randint(0, 2)
        velha[l][c] = 'O'
        quem_joga = 1
        jogadas += 1


def verificavitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        # verificador de linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != 'n'):
            break

        # verificador de colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != 'n'):
            break
        # verifica diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if(velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if (soma == 3):
            vitoria = s
            break

        # verifica diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 0
        while idiagc >= 0:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():
    global jogadas
    global quem_joga
    global maxjogadas
    global vit
    global velha
    jogadas = 0
    quem_joga = 1
    maxjogadas = 9
    vit = 'n'
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

tela()
while jogar_novamente == ('s').lower().strip()[0]:
        while True:
            print('    ')
            print('Jogador 1')
            print('    ')
            player1()
            tela()
            print('    ')
            print('jogador 2')
            print('      ')
            player2()
            tela()
            vit = verificavitoria()
            if vit != 'n' or jogadas >= maxjogadas:
                break
        print(f'{Fore.RED} FIM DE JOGO!!! {Fore.YELLOW}')
        if vit == 'X' or vit == 'O':
            print(f'Resultado: Jogador {vit} Venceu')
        else:
            print('Resultado, EMPATE')
        #cpu()
        jogar_novamente = str(input(f'{Fore.BLUE}Jogar Novamente? [s/n] {Fore.RESET}'))
        redefinir()
