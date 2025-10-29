import pyfiglet # type: ignore
from pyfiglet import Figlet # type: ignore
from colorama import Fore, Back, Style, init # type: ignore
import os
import time
import menu

#Inicializa o colorama para resetar as cores automaticamente
init(autoreset=True)

# Inicializa o Figlet e obtém as fontes disponíveis
f = Figlet()
fontes = f.getFonts()
uni = '\u1A27' #Caractere decorativo

# _____________________________________________
#  FUNÇÕES DE EXIBIÇÃO E ESTILOS DE TEXTO
#______________________________________________

def logo(texto: str, cor=Fore.YELLOW, fonte="slant") -> None:
    
    """"Exibe um logo em ASCII art com a fonte e cor especificadas."""
    
    ascii_art = pyfiglet.figlet_format(texto, font="slant")
    print(cor + ascii_art + Fore.RESET)

def descricao(texto: str, fonte="standard", cor=Fore.CYAN) -> None: 
    
    """Mostra uma descrição em ASCII art com a fonte e cor especificadas."""    
    
    print(cor + pyfiglet.figlet_format(texto, font=fonte) + Fore.RESET)

def descricao2(texto: str, cor=Fore.YELLOW) -> None:    
    
    """Mostra uma descrição simples com a cor especificada."""
    
    print(cor + texto + Fore.RESET)

def infoAlunos() -> None:
    
    """Mostra as informações dos alunos que fizeram o jogo."""
    
    alunos = ["Tiago Lucas", "Bianca Milani", "Ana Beatriz", "Ágata Silverio", "Victor Ribeiro"]
    print(Fore.MAGENTA + "Desenvolvido por:" + Fore.RESET)
    for aluno in alunos:
        print(f" {uni} {aluno}")
    print()

#______________________________________________
# FUNÇÕES DE JOGO / SISTEMA
#______________________________________________

def escolher_dificuldade() -> str:

    """Permite ao jogador escolher a dificuldade do jogo."""

    opcoes = {"1": "facil", "2": "medio", "3": "dificil"}
    while True:
        print("\nEscolha a dificuldade:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        escolha = input("\nDigite o número da dificuldade desejada: ")
        if escolha in opcoes:
            return opcoes[escolha]
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Fore.RESET)

def calcular_pontuacao(pontos: int, dificuldade:str) -> int:

    """Calcula a pontuação final com base na dificuldade escolhida."""

    multiplicador = {"facil": 1, "medio": 1.5, "dificil": 2}
    return (pontos * multiplicador.get(dificuldade, 1))

def iniciar_cronometro() -> float:

    """Retorna o tempo atual para iniciar o cronômetro."""
    
    return time.time()

def tempo_passado(inicio: float) -> float:
    
    """Retorna o tempo passado desde o início do cronômetro, em segundos."""
    
    return round(time.time() - inicio, 1)

def limpar_tela():
    os.system('cls')

#______________________________________________
# FUNÇÕES OPCIONAIS
#______________________________________________

def loading(mensagem="Carregando", duracao=2, simbolo=".") -> None:
    print(Fore.YELLOW + mensagem, end="", flush=True)
    for _ in range(int(duracao * 3)):
        time.sleep(0.3)
        print(simbolo, end="", flush=True)
    print(Fore.RESET)
    time.sleep(0.5)
    limpar_tela()
    
# ─────────────────────────────────────────────
#   TESTE RÁPIDO
# ─────────────────────────────────────────────
if __name__ == "__main__":
    limpar_tela()
    logo("PacMan in Python")
    descricao2("Bem-vindo!")
    infoAlunos()
    dificuldade = escolher_dificuldade()
    print(f"Sua dificuldade: {dificuldade}")
    loading("Iniciando o jogo")