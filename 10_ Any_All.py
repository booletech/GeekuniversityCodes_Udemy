"""
Any e All

ALL -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda e o iterável está vazio.
Exemplo:

print(all([0, 1, 2, 3, 4, 5]))
# False - > o zero é false na lista

print(all([1, 2, 3, 4, 5]))
# True -> Sem o zero, todos os outros são True

#Poderia ser uma tupla, um set, uma string

___________________________________
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))
# Utilizamos list Comprehension para verificar se os nomes na lista estão iniciando com a letra C
# True
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']
print(all(nome[0] == 'C' for nome in nomes))
#False


________________________

#Obs um iteravel vazio no all é True! em boolean ele é False!
print(all([letra for letra in 'eio' if letra in 'aeiou']))
#True

_______________________________

Any()
-> Retorna True se qualquer elemento do iterável for verdadeiro. Se for Vazio [] será False!


"""

print(any([0, False, {}, (), []]))  # False
print(any([0, False, {}, (), [], 1]))  # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
#True
print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0])) # Lista somente os pares
#True



