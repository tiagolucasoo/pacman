import utils as ut

ut.apagarTerminal()
ut.logo("PacMan Py")

ut.descricao2("Desenvolvido Por")
ut.infoAlunos()

name = input("""
    Para começar informe o seu nome: """)

print("""\n
    Dificuldade
    [1] - Fácil
    [2] - Normal
    [3] - Díficil\n
    """)

difficulty =  input("""
    Informe o n° da dificuldade escolhida: """)
