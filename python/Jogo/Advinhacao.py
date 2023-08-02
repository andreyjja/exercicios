
import random

def Jogar():
    print("###################################")
    print("bem vindo a jogo de advinhaçao")
    print("###################################")


    tentativas = int(input("Escolha a dificuldade: [1]facil [2]normal [3]dificil   :"))

    numero = random.randrange(1,101)

    rodadas = 1

    if tentativas == 1:
        tentativas = 20
    elif tentativas == 2:
        tentativas = 10
    else:
        tentativas = 5

    while(rodadas <= tentativas):
        print("tentativas {} de {} ".format(rodadas,tentativas))
        chute_str = input("Ola, digite um numero:  ")
        print("Seu Numero Foi:",chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 0 a 100")
            continue
        
        acertou = chute == numero
        menor   = chute > numero
        maior   = chute < numero

        if (acertou):
            break
        else:
            if menor:
                print("Você errou, o numero é menor")
            elif maior:
                print("Você errou, o numero é maior")
        rodadas += 1

    if chute == numero:
        print("Você ganhou O Numero era {}".format(numero))
    else:
        print("Você perdeu O Numero era {}".format(numero))

if __name__ == "__main__":
    Jogar()