import pyfiglet 
from pyfiglet import Figlet 
from colorama import Fore, Back, Style, init 
import os
import time

init(autoreset=True)

f = Figlet()
fontes = f.getFonts()
uni = '\u1A27'

def logo(texto: str, cor=Fore.YELLOW):
    ascii = pyfiglet.figlet_format(texto, font="slant")
    print(cor + ascii + Fore.RESET)

def descricao(texto: str, fonte="standard", cor=Fore.CYAN):
    print(cor + pyfiglet.figlet_format(texto, font=fonte) + Fore.RESET)

def descricao2(texto: str, cor=Fore.YELLOW) -> None:    
    print(cor + texto + Fore.RESET)

def infoAlunos() -> None:
    alunos = ["Tiago Lucas", "Bianca Milani", "Ana Beatriz", "Ágata Silverio", "Victor Ribeiro"]
    print(Fore.MAGENTA + "Desenvolvido por:" + Fore.RESET)
    for aluno in alunos:
        print(f" {uni} {aluno}")
    print()

def escolher_dificuldade():
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
    multiplicador = {"facil": 1, "medio": 1.5, "dificil": 2}
    return (pontos * multiplicador.get(dificuldade, 1))

def iniciar_cronometro() -> float:
    return time.time()

def tempo_passado(inicio: float) -> float:
    return round(time.time() - inicio, 1)

def limpar_tela():
    os.system('cls')

def loading(mensagem="Carregando", duracao=2, simbolo=".") -> None:
    print(Fore.YELLOW + mensagem, end="", flush=True)
    for _ in range(int(duracao * 3)):
        time.sleep(0.3)
        print(simbolo, end="", flush=True)
    print(Fore.RESET)
    time.sleep(0.5)
    limpar_tela()

if __name__ == "__main__":
    limpar_tela()
    logo("PacMan in Python")
    descricao2("Bem-vindo!")
    infoAlunos()
    dificuldade = escolher_dificuldade()
    print(f"Sua dificuldade: {dificuldade}")
    loading("Iniciando o jogo")

