import random



def Jogar():

    apresentacao()
    palavra_forca = carregar_palavra()

    palavra_acertadas = inicialicao_palavras(palavra_forca)
    print(palavra_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = escolher_letra()

        if(chute in palavra_forca):
            marcar_palavra(chute, palavra_acertadas, palavra_forca)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        acertou = "_" not in  palavra_acertadas
        enforcou = tentativas == 7
        print(palavra_acertadas)
        
    if (acertou):
        msg_vencedor()
    else:
        msg_perdedor(palavra_forca)
    
def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def msg_perdedor(palavra_forca):

    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_forca))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def apresentacao():
    print("###################################")
    print("bem vindo a jogo de forca")
    print("###################################")

def inicialicao_palavras(palavra):
    return ["_" for letra in palavra ]

def carregar_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_forca = palavras[numero].upper()
    return palavra_forca

def escolher_letra():
    chute = input("Qual a Letra :")
    chute = chute.strip().upper()
    return chute

def marcar_palavra(chute, palavra_acertadas, palavra_forca):
    index = 0
    for letra in palavra_forca:
        if(chute == letra):
            palavra_acertadas[index] = letra
        index += 1  
    return



if __name__ == "__main__":
    Jogar()
