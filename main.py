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
    jogo = game.pacman(usuario, dificuldade)

    if jogo == 'resetar':
        ut.limpar_tela()
        ut.loading("Reiniciando o Jogo...")
        continue

    elif isinstance(jogo, tuple) and jogo[0] == 'mudar':
        dificuldade = jogo[1]
        ut.limpar_tela()
        ut.loading(f"Alterando a dificuldade para {dificuldade}")
        continue

    else:
        ut.limpar_tela()
        ut.logo("Ate a proxima")
        break