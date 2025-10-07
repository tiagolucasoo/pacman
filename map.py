import os
import time
import keyboard
from colorama import Fore, Back, Style, init
import random
import utils

init(autoreset=True)


def limpar_tela():
    """Limpa a tela do terminal (funciona em Windows, Linux e Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_mapa(matriz, substituicoes, fantasmas):
    """Desenha o mapa, aplicando fundos dinâmicos para os fantasmas."""
    # Cria um dicionário para acesso rápido à posição dos fantasmas
    posicoes_fantasmas = {(f['y'], f['x']): f for f in fantasmas}
    
    mapa_para_imprimir = ""
    for y, linha in enumerate(matriz):
        for x, char in enumerate(linha):
            # Verifica se há um fantasma na coordenada atual
            if (y, x) in posicoes_fantasmas:
                fantasma_atual = posicoes_fantasmas[(y, x)]
                string_fantasma = substituicoes[fantasma_atual['char']]
                
                # --- A LÓGICA DINÂMICA ---
                # Se o fantasma está sobre o chão da casinha ('*'), usa fundo branco
                if fantasma_atual['deixou_para_tras'] == '*':
                    mapa_para_imprimir += Back.WHITE + string_fantasma
                else: # Senão, usa o fundo padrão
                    mapa_para_imprimir += Back.RESET + string_fantasma
            else:
                # Se não for um fantasma, usa a lógica normal
                mapa_para_imprimir += substituicoes.get(char, char)
        mapa_para_imprimir += '\n'
        
    print(mapa_para_imprimir, end="")

# Coloque esta nova função junto com as outras funções auxiliares
def encontrar_todas_posicoes(matriz, char):
    """Encontra todas as ocorrências de um caractere na matriz e retorna uma lista de coordenadas."""
    posicoes = []
    for i, linha in enumerate(matriz):
        for j, celula in enumerate(linha):
            if celula == char:
                posicoes.append({'y': i, 'x': j})
    return posicoes

# --- 2. CONFIGURAÇÃO INICIAL DO JOGO ---

# Dicionário de substituições. Fica mais organizado que vários .replace()
substituicoes_cores = {
    # Itens do cenário
    '#': Back.RESET + Fore.BLUE + '\u2588',
    '.': Back.RESET + Fore.WHITE + '.',
    '+': Back.RESET + Fore.YELLOW + '\u1A27',
    '*': Back.WHITE + ' ', # O chão da casinha continua com fundo branco

    # Fantasmas agora só definem a cor da frente e o caractere
    '8': Fore.RED + '\u03A9',
    '7': Fore.CYAN + '\u03A9',
    '6': Fore.GREEN + '\u03A9',
    '5': Fore.MAGENTA + '\u03A9',
}

mapa_string = """
A ######################################################
B #............#............##.........................#
C #.#.##########.##########.##.##########.##########.#.#
D #.#.##########.##########.##.##########.##########.#.#
E #....................................................#
F #.#.##.##############.##########.##############.##.#.#
G #...##....##....###...##..##..##...###....##....##...#
H #...##....##....###...##..##..##...###....##....##...#
I #...##....##....###...##..##..##...###....##....##...#
J ######.##.##.###.##.##############.##.###.##.##.######
E #.........##.........................................#
K #.......####...........###**###.........#....#.......#
L #.......######.........#*8**7*#.........#....#.......#
M #.......#....#.........#*6**5*#.........######.......#
N #.......#....#.........########...........####.......#
O #.........................................##.........#
P ######.##.##.###.##.##.###########.##.###.##.##.######
Q #...##....##....###...##..##..##...###....##....##...#
R #...##....##....###...##..##..##...###....##....##...#
S #...##....##....###...##..##..##...###....##....##...#
T #.#.##.##########.###.##########.###.##########.##.#.#
U #.................#####........#####.................#
V #.......................#.+.#....................#...#
W #.#.##########.##########.#############.##########.#.#
X #.#.##########.##########.##.##########.##########.#.#
Y #............#............##.........................#
Z ######################################################
"""

# Converte a string do mapa em uma matriz (lista de listas de caracteres)
mapa_matriz = [list(linha) for linha in mapa_string.strip().split('\n')]

# Encontra a posição inicial do Pac-Man ('P')
pacman_y, pacman_x = -1, -1
for i, linha in enumerate(mapa_matriz):
    if '+' in linha:
        pacman_y = i
        pacman_x = linha.index('+')
        break

fantasmas = []
codigos_fantasmas = ['8', '7', '6', '5'] # Lista com o ID de cada fantasma

for codigo in codigos_fantasmas:
    posicoes = encontrar_todas_posicoes(mapa_matriz, codigo)
    for pos in posicoes:
        fantasmas.append({
            'y': pos['y'],
            'x': pos['x'],
            'char': codigo,  # <-- Usa o código correto para cada fantasma
            'deixou_para_tras': '*' # Fantasmas começam em cima de '*'
        })

# --- 3. O GAME LOOP ---

while True:
    # Desenha o estado atual do mapa
    limpar_tela()
    utils.logo("PacMan Py")
    desenhar_mapa(mapa_matriz, substituicoes_cores, fantasmas)

    # Pequena pausa para controlar a velocidade do jogo
    time.sleep(0.1)

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

    # --- 4. CAPTURA DE ENTRADA E LÓGICA DE MOVIMENTO ---
    if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
        proximo_y -= 1
    elif keyboard.is_pressed('down') or keyboard.is_pressed('s'):
        proximo_y += 1
    elif keyboard.is_pressed('left') or keyboard.is_pressed('a'):
        proximo_x -= 1
    elif keyboard.is_pressed('right') or keyboard.is_pressed('d'):
        proximo_x += 1
    elif keyboard.is_pressed('esc'): # Adiciona uma forma de sair do jogo
        break

    # --- 5. ATUALIZAÇÃO DO MAPA ---

    # Verifica se a próxima posição é válida (não é uma parede '#')
    if mapa_matriz[proximo_y][proximo_x] != '#':
        # Apaga o Pac-Man da posição antiga
        mapa_matriz[pacman_y][pacman_x] = ' '
        # Atualiza as coordenadas
        pacman_y, pacman_x = proximo_y, proximo_x
        # Coloca o Pac-Man na nova posição
        mapa_matriz[pacman_y][pacman_x] = '+'

print("Jogo finalizado!")