"""
Trabalhando com módulos Built-in (Módulos integrados que já vem instalados no python.

Quando realizamos a instalação do python instalamos todos os módulos Built in

Para que a memória de utilização do python não sobrecarregue devemos "chamar" o módulo
que vamos utilizar. import módulo

https://docs.python.org/3/py-modindex.html


________________________
IMPORTANDO TODO O MÓDULO
_______________________________________________________
import random

print(random.random())



__________________________
ALIAS
_______________________________________________________
# utilizando Alias (Apelidos) para módulos/funções
# utilize as antes do apelido


from random import random as rdm
print(rdm())


________________________________________
UTILIZANDO *
_____________________________________________________________

# Podemos importar todas as funções de um módulo utilizando *
from random import *
print(random())



______________________
APELIDOS PARA FUNÇÕES:
________________________________________________________

# Exemplo1
from random import randint as rdi
print(rdi(32, 45))



# Exemplo2
from random import randint as rdi, random as rdm # Apelidei duas funções !!!
print(rdi(32, 45))



"""

# Costumamos colocar tuple em multiplos imports de um mesmo módulo:
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(3, 7))

lista = ['Julio', 'Cesar', 'Python', 'oi']
shuffle(lista)
print(lista)

print(choice('Jubilado'))




