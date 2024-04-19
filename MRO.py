"""
POO - MRO -> Method Resolution Order

Resolução de ordem de métodos
    Ordem de execução dos métodos

Em python podemos conferir a ordem de três formas
  Via propriedade da classe
  Via método
  Via help

"""


class Animal:  # Classe base ou Classe Pai

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


# Vamos criar duas Classes que herdam de Animal:


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f' {self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da Terra!'


class Pinguim(Terrestre, Aquatico):  # Verificar a ordem de Herança
    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('tux')
print(tux.cumprimentar())  # ??? Eu sou tux da Terra! ou Eu sou tux do mar! ???  Method Resolution Order - MRO

"""
class Pinguim(Aquatico, Terrestre):
Eu sou tux do mar!

class Pinguim(Terrestre, Aquatico):
Eu sou tux da Terra!


Pinguim.__mro__
Out[9]: (MRO.Pinguim, MRO.Terrestre, MRO.Aquatico, MRO.Animal, object)

"""