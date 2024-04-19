"""
POO - Heranca Multipla

# Vimos em outras aulas que podemos fazer o reaproveitamento de classes usando outras classes
# Uma classe herdada de outra classe , recebe todos os outros atributos e métodos de outras classes

Heranca multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

Para entendermos melhor vamos demonstrar:

Obs: A herança múltipla pode ser feita de duas maneiras:
1- Por multiderivação direta
2- Por multiderivação indireta

# Falamos que uma classe deriva de outra quando uma classe herda outra.


# Exemplo: Multiderivação direta:
# Não são classes reais, vamos apenas dar um exemplo:


class Base1:
    pass  # (atributos e métodos)


class Base2:
    pass  # (atributos privados e de instancia e métodos, etc)


class Base3:
    pass


class Multiderivada (Base1, Base2):
    pass

# Exemplo: Multiderivação indireta:


class Base1:
    pass


class Base2 (Base1):
    pass


class Base3(Base2):
    pass

class Multiderivada(Base3)
    pass

# Não importa de a derivação é direta ou indireta. A classe que realizar a herança herdará todos
os atributos e métodos das super classes.

"""


# Vamos a um exemplo real:


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


class Pinguim(Aquatico, Terrestre):  # Verificar a ordem de Herança
    def __init__(self, nome):
        super().__init__(nome)


# Testando:


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # ??? Eu sou tux da Terra! ou Eu sou tux do mar! ???  Method Resolution Order - MRO

# Como descobrir se um objeto é uma instância de uma classe?

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')  # True
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')  # True
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')  # True
print(f'Tux é instância de Object? {isinstance(tux, object)}')  # True
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')  # True



