"""
Zip

zip() -> Cria um iteravel (Zip Object) que agrega elemento de cada um ods iteraveis passados como
entrada em pares.


# Exemplos:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
# <zip object at 0x00000297C830B780>

# Podemos gerar uma lista, uma tupla, um conjunto ou um dicionário

zip1 = zip(lista1, lista2)
print(list(zip1))  # [(1, 4), (2, 5), (3, 6)]

zip1 = zip(lista1, lista2)
print(tuple(zip1))  # ((1, 4), (2, 5), (3, 6))

zip1 = zip(lista1, lista2)
print(set(zip1))  # {(2, 5), (1, 4), (3, 6)}

zip1 = zip(lista1, lista2)
print(dict(zip1))  # {1: 4, 2: 5, 3: 6}


# E se tivermos uma lista maior ??

lista3 = [7, 8, 9, 10]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# O zip ignora os valores da lista maior pois considera o tamanho da menor como padrão!




# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))
# [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
# [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


"""


#Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# Vamos gerar um dicionario com as notas dos estudantes
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
# {'maria': 98, 'pedro': 91, 'carla': 78}

# Podemos utilizar o map() para fazer isso:
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))


