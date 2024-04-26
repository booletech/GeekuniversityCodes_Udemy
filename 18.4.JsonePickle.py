"""
Json e Pickle

JSON -> Javascript Object Notation (Tipo de arquivo MUITO utilizado em API's de Empresas
API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, etc) e terceiros

_______________________

import json

ret = json.dumps(['Produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
# ret = json.dumps(['Lista', { Dicionario : (tupla com os dados))})
# Temos uma lista contendo dois itens: Produto, um dicionário com chave Playstation4 e valores (características)

print(type(ret))  # <class 'str'>
print(ret)  # ["Produto", {"Playstation 4": ["2TB", "Novo", "220V", 2340]}]

# Repare que a impressão saiu um pouco diferente:
# As aspas simples '' foram substituídas por aspas duplas ""
# Isso acontece por que Json trabalha apenas com aspas duplas
# utilizamos o dumps para formatar

____________________________________-


import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando um objeto


Felix = Gato('Felix', 'RND')
print(Felix.__dict__)
# {'_Gato__nome': 'Felix', '_Gato__raca': 'RND'}

ret = json.dumps(Felix.__dict__)
print(ret)
# {"_Gato__nome": "Felix", "_Gato__raca": "RND"}


______________________________________________________
import jsonpickle
# Integrando o json com o pickle
# pip install jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando um objeto


Felix = Gato('Felix', 'RND')

ret = jsonpickle.encode(Felix)
print(ret)
# {"py/object": "__main__.Gato", "_Gato__nome": "Felix", "_Gato__raca": "RND"}

# Nada mudou na classe, o diferencial é que precisamos instalar o pacote jsonpickle
# Ao invés de utilizarmos json.dumps utilizamos jsonpickle.encode(Felix) sem o dict
# Temos chave:valor no print(ret)
# Esse json é um objeto da classe Gato

____________________________________________________________-
import jsonpickle

# ABRINDO O ARQUIVO PARA ESCRITA:
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando um objeto
# Abrindo o arquivo para escrita:

Felix = Gato('Felix', 'RND')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# NESSE CASO NÃO É UM ARQUIVO CSV!
# Afunção encode modela nosso objeto para o formato JSONPICKLE

_____________________________________________________




"""

import jsonpickle

# ABRINDO O ARQUIVO PARA ESCRITA:
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


# Instanciando um objeto
# Abrindo o arquivo para escrita:

Felix = Gato('Felix', 'RND')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# NESSE CASO NÃO É UM ARQUIVO CSV!
# A função encode modela nosso objeto para o formato JSONPICKLE

