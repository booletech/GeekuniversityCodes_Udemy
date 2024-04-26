"""
Conhecendo Pickle

A função do pyckle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> objeto python

Este processo é chamado de serialização / deserialização

#Obs: O método Pickle não é seguro contra dados maliciosos e desta forma não é recomendado
trabalhar com arquivos pickle vindo de outras pessoas desconhecidas.


"""

# *1 Extensão pickle é utilizada para sinalizar, não é obrigatório; wb → write binary
# *2 Método dump recebe dois parâmetros (objeto, arquivoparaescrita)

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo!')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando!')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo!')


"""
# Fazendo a escrita de arquivos pickle:
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:  # *1
    pickle.dump((felix, pluto), arquivo)  # *2
"""

# Fazendo a leitura de dados em arquivos pickle:
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato se chama {gato._Animal__nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro se chama {cachorro._Animal__nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')

    