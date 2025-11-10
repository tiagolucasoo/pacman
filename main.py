import utils as ut
import menu
import game

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
    
    elif isinstance(jogo, tuple) and jogo[0] == 'game_over':
        pontuacao_final = jogo[1]
        tempo_jogado = jogo[2]

        ut.limpar_tela()
        menu.Game_Over()
        print(f"\n    Ops {usuario}, você perdeu!")
        print(f"    Pontuação Final: {pontuacao_final}")
        print(f"    Tempo: {tempo_jogado}s")
        break

    elif isinstance(jogo, tuple) and jogo[0] == 'vitoria':
        pontuacao_final = jogo[1]
        tempo_jogado = jogo[2]

        ut.limpar_tela()
        menu.Vitoria()
        print(f"\n    PARABÉNS {usuario}, VOCÊ GANHOU!")
        print(f"    Pontuação Final: {pontuacao_final}")
        print(f"    Tempo: {tempo_jogado}s")
        break

    else:
        ut.limpar_tela()
        ut.logo("Ate a proxima")
        break