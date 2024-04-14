"""
Módulo Collections - Counter (contador)

COLLECTIONS  -->  Conhecido por hIgh performance container date types
Provê implementações alternativas:

Counter --> Recebe um iterável como parâmetro e cria um objeto do tipo Collections counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor a quantidade e ocorrências desse elemento.



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Utilizando o counter:

# importe o counter do módulo collections:
from collections import Counter

# Podemos utilizar qualquer iterável, aqui utilizaremos uma lista:
lista = [1, 3, 4, 5, 6, 7, 5, 6, 4, 3, 2, 7, 8, 9, 5, 4, 9, 45, 67, 56, 78, 34, 25, 103, 45, 67, 34, 56, 67, 87, 100]

# PROBLEMA 1: Liste cada um dos elementos e quantas vezes ele se repete:
# Utilizando o counter:
res = Counter(lista)
print(type(res))
print(res)

# Counter({4: 3, 5: 3, 67: 3, 3: 2, 6: 2, 7: 2, 9: 2, 45: 2, 56: 2, 34: 2, 1: 1, 2: 1, 8: 1, 78: 1, 25: 1, 103: 1,
# 87: 1, 100: 1})
# Veja que para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrências.



<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

from collections import Counter

#PROBLEMA 2: Conte os caracteres de uma string incluindo a quantidade de espaços.
#podemos utilizar o counter com qualquer iteravel, inclusive strings

print(Counter('Julio Cesar da Silva Jubilado'))
# Counter({' ': 4, 'a': 4, 'l': 3, 'i': 3, 'J': 2, 'u': 2, 'o': 2, 'd': 2, 'C': 1, 'e': 1, 's': 1, 'r': 1, 'S': 1,
# 'v': 1, 'b': 1})



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


"""


from collections import Counter

texto = """A lua brilhava no céu noturno,
Enquanto o vento soprava suavemente.
No silêncio da noite, ouviu-se um murmúrio distante,
E um gato preto passeava pela rua.
Os grilos cantavam em coro,
E as estrelas cintilavam no infinito."""

#Se colocarmos texto.split teremos uma lista com cada uma das palavras:
palavras = texto.split()
print(palavras)


#Vamos saber quais palavras estão no texto (sem repeti-las) e vamos saber a quantidade de cada uma:
res = Counter(palavras)
print(res)

#Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(3))









