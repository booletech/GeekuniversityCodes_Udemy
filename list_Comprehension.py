"""
# List comprehension
- utilizando list comprehension nós podemos gerar novas listas com dados processados
a partir de outro iterável

# Sintaxe da List comprehension
#inicie com conchetes []
[dado for dado in iterável]


# exemplos
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [n * 10 for n in num]
print(res)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

"""
'''
Para entender melhor o que está acontecendo vamos dividir melhor a expressão
- A primeira parte: for n in num (Para cada n (numero) na lista num
- A segunda parte: n * 10 (multiplica cada n numero na lista por 10)
'''
"""

res = [n / 2 for n in num]
print(res)


def funcao(valor):
    return valor * valor

res = [funcao(n) for n in num]
print(res)


_____________________________________________________

# List Comprehensions VS Loop

# Loop

#Temos a seguinte lista:
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Vamos dobrar os números

#Primeiro criamos outra lista para os números dobrados :
numeros_dobrados = []
for n in num:
    n_dob = n * 2
    numeros_dobrados.append(n_dob)
print(numeros_dobrados)
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#Utilizando List Comprehensions
print([n * 2 for n in num])
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




"""


# Outros exemplos:
# 1
# nome = 'Julio Cesar'
# print([letra.upper() for letra in nome])
# ['J', 'U', 'L', 'I', 'O', ' ', 'C', 'E', 'S', 'A', 'R']


# 2

'''
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julio', 'joão', 'vinicius', 'mauro']
print([caixa_alta(amigo) for amigo in amigos])
# ['Maria', 'Julio', 'João', 'Vinicius', 'Mauro']
'''


#3
'''
print([n * 3 for n in range(1, 21)])
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
'''

#4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# [False, False, False, True, True, True]

#5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
#['1', '2', '3', '4', '5']
