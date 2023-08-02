import Advinhacao
import forca

print("###################################")
print("##########Menu De jogos############")
print("##########escolha um jogo##########")
print("[1]Advinhação [2]forca ")
jogo = int(input("Qual Jogo?  :"))
print("###################################")

if jogo == 1:
    print("adivinhação")
    Advinhacao.Jogar()
elif jogo == 2:
    print("forca")
    forca.Jogar()
