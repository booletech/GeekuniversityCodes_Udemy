"""
O método Super()
- O método Super() se refere à super classe
- Quando temos uma classe base e uma classe especifica herda dessa classe base, lá na classe específica
fazemos acesso aos elementos da super classe através do super()
- Com o super() podemos ter acesso a qualquer elemento da classe pai!
Vamos relembrar:

"""


class Animal:
    # construtor
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
    #métodos

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):  # O Gato herda de Animal
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)  # RECOMENDADO!
        self.__raca = raca


# Vamos testar a classe e ver se está ok:
# Instanciamos um objeto do tipo Gato,
felix = Gato('Felix', 'Felino', 'angora')
felix.faz_som('miau')  # Método faz_som

# O Felix fala miau
