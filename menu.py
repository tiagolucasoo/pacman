import time
import sys

def iniciar_jogo():
    print("Hora de começar a jogar!")
    time.sleep(1)
    menu()

def fase_atual():
    print("O jogo continua.\n")

def menu():
    menu_texto = """
======== MENU ========
[1] - Pausar
[2] - Continuar
[3] - Resetar
[4] - Mudar a dificuldade
[5] - Sair
======================
"""
    print(menu_texto)

    opcoes_menu = {
        '1': pausar,
        '2': continuar,
        '3': resetar,
        '4': mudar_dificuldade,
        '5': sair
    }

    while True:
        escolha = input("Escolha uma opção do menu: ")

        if escolha in opcoes_menu:

            opcoes_menu[escolha]() 
            break

        else:
            print("Opção inválida. Tente novamente.")

def pausar():
    print("\nJogo pausado. Aperte ENTER para continuar...")
    input()

    continuar()
    fase_atual()

def continuar():
    print("Retornando para fase... \n")

def resetar():
    print("\nJogo resetado. Voltando ao início...") 

    iniciar_jogo()

def mudar_dificuldade():
    tipo_dificuldade = """
______ Nível de Dificuldade ______

1. Fácil
2. Médio
3. Difícil
__________________________________
"""
    print(tipo_dificuldade)

    while True:
        nivel = input("Informe o nº da dificuldade escolhida: ")

        if nivel in ['1', '2', '3']:
            dificuldade = int(nivel)
            nomes_dificuldade = ['Fácil', 'Médio', 'Difícil']
            print(f'\nA dificuldade foi alterada para [{nomes_dificuldade[dificuldade - 1]}].')
            resetar()
            break

        else:
            print("Opção indisponível. Tente novamente...")

def sair():

    while True:
        confirmacao = input("\nTem certeza que deseja sair? (S/N): ").strip().upper()

        if confirmacao == 'S':
            print("Você saiu do jogo. O seu progresso foi salvo.")
            print("Encerrando o programa...")
            sys.exit()

        elif confirmacao == 'N':
            print("Saída cancelada. Voltando ao menu principal.")
            menu()
            break

        else:
            print("Opção inválida. Use 'S' para Sim ou 'N' para Não.")

if __name__ == "__main__":
    menu()