class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} -  {self.likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - Minutos:{self.duracao} -  {self.likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - Temporadas:{self.temporadas} -  {self.likes} likes'



class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self.listagem)

    def __getitem__(self, item):
        return self._programas[item]

