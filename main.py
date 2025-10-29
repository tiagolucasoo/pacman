import utils as ut
import menu
import game

# Chama a função de Limpar 
ut.limpar_tela()
ut.logo("PacMan Py")
ut.infoAlunos()

usuario = menu.validacao_nome()
dificuldade = ut.escolher_dificuldade()

while True:
    game.pacman(usuario, dificuldade)