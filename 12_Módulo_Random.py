"""
O que são módulos?

-> Em python, módulos são outros arquivos python
-> Cada arquivo gerado até agora aqui, são módulos

Vamos entender melhor com o módulo random

Módulo random -> Funções que geram números pseudoaleatórios

Existem duas formas de utilizar:

1 -> Simplesmente importamos:
# Ao realizar todo o módulo todas as funções atributos classes e propriedades ficaram em memória. NÃO RECOMENDADO!
# Caso você ja saiba qual vai utilizar :


2 -> Importar apenas a função que vai utilizar; Apenas uma função específica. RECOMENDADO!

print(random.random())

#ou no ínício:

from random import random



# random gera um número aleatório entre 0 e 1
# para utilizar a função nós colocamos o nome do pacote e da função separados com ponto (.)
# NÃO CONFUNDA! Existe a função random e o pacote random!

Exemplo:

# Forma Recomendada
from random import random # Do módulo random, importe a função random

for i in range(10):
    print(random())
# mostrará dez números aleatórios que ficam entre 0 e 1
#RANDOM É MUITO UTILIZADO EM INTELIGÊNCIA ARTIFICIAL (REDES NEURAIS)

____________________________________
# uniform() -> Gera um número pseudoaleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluído
# Gerará uma lista de 10 números entre 3 e 7 (Não inteiros)

_____________________________________________________
# randint() -> Gera valores inteirosaleatórios entre os estabelecidos.
# Gerador de apostas mega sena
from random import randint

for i in range(6):  # Gera 6 números
    print(randint(1, 61), end=', ') # Valores inteiros entre 1 e 60
____________________________________________________

# Choice() -> mostra um valor aleatório de um iterável
from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogadas))

___________________________________________________

# Shuffle() -> Embaralha dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)  # ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
shuffle(cartas) # Embaralha as cartas
print(cartas)  # Exibe o novo resultado


"""






