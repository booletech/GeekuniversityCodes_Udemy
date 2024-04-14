"""
Módulo Collections: Ordered Dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict
_________________________
# Em um dicionário a ordem dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print (dicionario)
_________________________

# O ordered dict garante que o que foi inserido ficará na mesma ordem
# Fazendo o import
from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd':4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')
__________________________

# Entendendo as diferenças entre Dict e Ordered Dict
# Dicionários Comuns
dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}
print(dict1 == dict2) # True/False ???
#True
# Desconsiderou a ordem e comparou os valores apenas

__________________________________________________________
from collections import OrderedDict
# Dicionários Ordenados (Ordered Dict)
odict1 = OrderedDict({'a':1, 'b':2})
odict2 = OrderedDict({'b':2, 'a':1})
print(odict1 == odict2) # True/False ???
#False
# Considerou a ordem, que esta irregular

___________________________________________________________


"""


