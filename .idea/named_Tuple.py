"""
Módulo Collections - Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple


#Criamos um tipo de dado nosso
____________________________________
#REvisando Tuple
tupla = (1, 2, 3)
print(tupla[1])
# 2
__________________________________

Named Tuple -> Tupla Nomeada
São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""
#importando

from collections import namedtuple

#Qual será o nome da tupla e quais serão seus parâmetros?

# Forma 1 -> Declaração named Tuple
cachorro = namedtuple('cachorro','idade raca nome')  #ParÂmetros separados por espaço

#Forma 2 -> Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')  #ParÂmetros separados por virgula

#Forma 3 -> Declaração Named tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome']) #Criamos uma lista com os parâmetros

#Usando


Ray = cachorro(idade=2, raca='chow-chow', nome = 'Ray')

#Acessando os dados

#FORMA 1
print(Ray[0]) #idade
print(Ray[1]) #raca
print(Ray[2]) #nome

#FORMA 2
print(Ray.idade) #idade
print(Ray.raca)  #Raça
print(Ray.nome)  #Nome


#Podemos utilizar o index para saber qual a posição do valor
print(Ray.index('chow-chow'))
#1

#Quantas vezes determinado valor aparece?
print(Ray.count('chow-chow'))
#1




