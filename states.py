import utils
# Funções de mudança de Status
#	states.py	#
#	- Padrão state, os diferentes estados do jogo
#	- MenuPrincipal
#	- Jogando
#	- Pausado
#	- GameOver
#	- Vitoria

def Game_Over():
    return utils.logo("Game Over")

def Vitoria():
    return utils.logo("Vitoria")

Game_Over()
Vitoria()