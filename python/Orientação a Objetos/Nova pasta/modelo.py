class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._like
    
    def dar_likes(self):
        self._like += 1
        return



class Filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._like}"


class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._like}"

class playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

arqueiro = Serie("arqueiro", 1999, 3)
flash = Serie("flash", 2000, 3)
vingadores = Filme("vingadores", 2000, 60)
flash.dar_likes()


filme_serie = [flash,vingadores, arqueiro]

playlist_fim_de_semana = playlist("playlist_fim_de_semana", filme_serie)


print(f"tamanho da playlist : {len(playlist_fim_de_semana)}")

for playlist in playlist_fim_de_semana:
    print(playlist)