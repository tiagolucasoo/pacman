import pyfiglet
from pyfiglet import Figlet

def logo(texto):
    return print(pyfiglet.figlet_format(str(texto), font="slant"))

logo("PacMan Python")
logo("P")

f = Figlet()
fontes = f.getFonts()

'''
def testefontes(texto, fonte):
    return print(pyfiglet.figlet_format(str(texto), font=str(fonte)))
#3 é bom | 31 | 32 | 60 | 64 jogador
testefontes("Tiagolucasoo - 1,2,3 Pontos", fontes[130])
'''