import os
import time
import keyboard
from colorama import Fore, Back, Style, init
import random
import utils
from map import mapa_original

def pacman(usuario, dificuldade):
    init(autoreset=True)
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def desenhar_mapa(matriz, substituicoes, fantasmas):
        """Desenha o mapa, aplicando fundos dinâmicos para os fantasmas."""
        # Cria um dicionário para acesso rápido à posição dos fantasmas
        posicoes_fantasmas = {(f['y'], f['x']): f for f in fantasmas}
        
        mapa_para_imprimir = ""
        for y, linha in enumerate(matriz):
            for x, char in enumerate(linha):
                if (y, x) in posicoes_fantasmas:
                    fantasma_atual = posicoes_fantasmas[(y, x)]
                    string_fantasma = substituicoes[fantasma_atual['char']]

                    if fantasma_atual['deixou_para_tras'] == '*':
                        mapa_para_imprimir += Back.WHITE + string_fantasma
                    else:
                        mapa_para_imprimir += Back.RESET + string_fantasma
                else:
                    mapa_para_imprimir += substituicoes.get(char, char)
            mapa_para_imprimir += '\n'
            
        print(mapa_para_imprimir, end="")

    def encontrar_todas_posicoes(matriz, char):
        """Encontra todas as ocorrências de um caractere na matriz e retorna uma lista de coordenadas."""
        posicoes = []
        for i, linha in enumerate(matriz):
            for j, celula in enumerate(linha):
                if celula == char:
                    posicoes.append({'y': i, 'x': j})
        return posicoes

    substituicoes_cores = {
        '#': Back.RESET + Fore.YELLOW + '\u2588',
        '.': Back.RESET + Fore.WHITE + '.',
        '+': Back.RESET + Fore.YELLOW + '\u1A27',
        '*': Back.WHITE + ' ',

        '8': Fore.RED + '\u03A9',
        '7': Fore.CYAN + '\u03A9',
        '6': Fore.GREEN + '\u03A9',
        '5': Fore.MAGENTA + '\u03A9',
    }

    mapa_string = mapa_original
    mapa_matriz = [list(linha) for linha in mapa_string.strip().split('\n')]

    pacman_y, pacman_x = -1, -1
    for i, linha in enumerate(mapa_matriz):
        if '+' in linha:
            pacman_y = i
            pacman_x = linha.index('+')
            break

    fantasmas = []
    codigos_fantasmas = ['8', '7', '6', '5']

    for codigo in codigos_fantasmas:
        posicoes = encontrar_todas_posicoes(mapa_matriz, codigo)
        for pos in posicoes:
            fantasmas.append({
                'y': pos['y'],
                'x': pos['x'],
                'char': codigo,
                'deixou_para_tras': '*'
            })

    while True:
        limpar_tela()
        utils.logo("PacMan Py")
        print(f"Usuário: {usuario}")
        print(f"Dificuldade: {dificuldade}\n\n")
        desenhar_mapa(mapa_matriz, substituicoes_cores, fantasmas)

        time.sleep(0.05) # Fácil 0.15

        for fantasma in fantasmas:
            # Define as possíveis direções (delta_y, delta_x)
            movimentos_possiveis = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Cima, Baixo, Esquerda, Direita
            dy, dx = random.choice(movimentos_possiveis)
            proximo_y, proximo_x = fantasma['y'] + dy, fantasma['x'] + dx

            # Verifica se a próxima posição é válida (não é uma parede)
            if mapa_matriz[proximo_y][proximo_x] not in ['#', '8', '7', '6', '5']:
                    mapa_matriz[fantasma['y']][fantasma['x']] = fantasma['deixou_para_tras']
                    fantasma['deixou_para_tras'] = mapa_matriz[proximo_y][proximo_x]
                    fantasma['y'], fantasma['x'] = proximo_y, proximo_x
                    mapa_matriz[fantasma['y']][fantasma['x']] = fantasma['char']

        # Posição futura, começa igual à atual
        proximo_y, proximo_x = pacman_y, pacman_x

        if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
            proximo_y -= 1
        elif keyboard.is_pressed('down') or keyboard.is_pressed('s'):
            proximo_y += 1
        elif keyboard.is_pressed('left') or keyboard.is_pressed('a'):
            proximo_x -= 1
        elif keyboard.is_pressed('right') or keyboard.is_pressed('d'):
            proximo_x += 1
        elif keyboard.is_pressed('esc'):
            break

        # Verifica se a próxima posição é válida (não é uma parede '#')
        if mapa_matriz[proximo_y][proximo_x] != '#':
            # Apaga o Pac-Man da posição antiga
            mapa_matriz[pacman_y][pacman_x] = ' '
            # Atualiza as coordenadas
            pacman_y, pacman_x = proximo_y, proximo_x
            # Coloca o Pac-Man na nova posição
            mapa_matriz[pacman_y][pacman_x] = '+'

    print("Jogo finalizado!")