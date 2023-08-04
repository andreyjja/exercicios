class Conta:

    def __init__(self, numero, nome, saldo, limite):
        print("Sua Conta {}".format(self))
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Seu Saldo é de {} Senhor(a) {}".format(self.__saldo, self.__nome))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        valor_dispobivel = self.saldo + self.limite
        return  valor_sacar <= valor_dispobivel



    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(self.__limite)) 

    def tranferir(self,valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite


    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

