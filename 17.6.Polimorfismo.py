"""
POO - Polimorfismo (Muitas formas)
-> Objetos que podem ser comportar de formas diferentes



"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método!')

    def comer(self):
        print(f'{self.__nome} está comendo!')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau ')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala snick snick')


# testes:

Felix = Gato('Felix')
Felix.comer()
Felix.falar()

Pluto = Cachorro('Pluto')
Pluto.comer()
Pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()  # NotImplementedError: A classe filha precisa implementar este método! (*44)

# Quando reimplementamos um método presente na classe pai em classes filhas estamos realizando
# uma sobrescrita de métodos -> Overriding
# O overriding é a melhor representação do polimorfismo.

