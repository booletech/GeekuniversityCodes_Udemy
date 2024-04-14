"""
Dictionary Comprehension

Pense o seguinte:
Quando criamos uma lista fazemos:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Utiliza conchetes


Quando criamos uma tupla fazemos:
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Utiliza parenteses ou nada


Quando criamos um conjunto (set) fazemos:
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # Utiliza chaves


Quando criamos um dicionário fazemos:
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4 } # Utiliza conchetes chave:valor

# {chave:valor for valor in iteravel} # Dictionary Comprehension
# [valor for valor in iteravel] #List comprehension

#Exemplos:
n = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {c:v ** 2 for c, v in n.items()}
#n = numero
#c = chave
#v = valor
print(quadrado) # {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

_________________________________________________________________-
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quad = {valor: valor**2 for valor in ns}
print(quad)
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

____________________________________________________________________

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)


______________________________________________________________________



"""
# Exemplos
# Lógica condicional

ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = {n: ('par' if n % 2 == 0 else 'impar') for n in ns}
print(res)
#{1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar', 6: 'par', 7: 'impar', 8: 'par', 9: 'impar', 10: 'par'}
