import pyfiglet
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init
import os

f = Figlet()
fontes = f.getFonts()
uni = '\u1A27'

def logo(texto):
    ascii = pyfiglet.figlet_format(str(texto), font="slant")
    return print(Fore.YELLOW + ascii + Fore.RESET)

def descricao(texto, fonte):
    return print(pyfiglet.figlet_format(str(texto), font=str(fonte)))

def descricao2(texto):
    return print(Fore.YELLOW + texto + Fore.RESET)

def infoAlunos():
    #utils.descricao("Alunos", "mini")
    return print(f"""
    {uni} Tiago Lucas
    {uni} Bianca Milani
    {uni} Ana Beatriz
    {uni} Ágata Silverio
    {uni} Nome Sobrenome""")

def apagarTerminal():
    os.system('cls')

