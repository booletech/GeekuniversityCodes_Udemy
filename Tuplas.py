"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por Parênteses ()
2 - As tuplas são IMUTÁVEIS ! Ao se criar uma tupla ela nõ muda. Toda operação em uma tupla gera uma nova
Tupla.




# Cuidado 1: As tuplas sõo representadas por (), mas veja:

# Com parênteses:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))  # Class 'Tuple'

# Sem Parênteses:
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))  # Class 'Tuple"

#Cuidado 2: Tuplas com 1 elemento
tupla3 = (4)
print(tupla3)
print(type(tupla3))  # Class 'int' #Não é uma tupla!!!

tupla4 = (4,)  # Isso é uma tupla !!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

#Conclusão: Podemos concluir que tuplas são definidas pela VIRGULA e não pelo uso do Parênteses
(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla


#Gerar tupla usando Range (dinamicamente) Parâmetros range (inicio, fim, passo):
tupla = tuple(range(11))
print(tupla)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#Desempacotamento de Tuplas:

tupla = ('Julio Cesar', 'Humano', '30 Anos')
Nome, Especie, idade = tupla
print(Nome)
print(Especie)
print(idade)

#Métodos para adição e remoção de elementos nas Tuplas não existem dado o fato das tuplas serem imutáveis
# Se os valores forem todos inteiros e reais podemos usar SOMA, VALOR MAX e VALOR MIN, Tamanho
# Em TAMANHO não importa o tipo de valor

tupla = (1, 2, 3, 4, 5, 6, "b")
print(len(tupla))  # 7
print(max(tupla))  # TypeError: '>' not supported between instances of 'str' and 'int'


# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)



#Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)  # Verifica se 3 está contido na tupla
print(33 in tupla)


#iterando sobre tuplas
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for n in tupla:
    print(n + 1, n-1, n+n, n*n)

for indice, valor in enumerate(tupla):
    print(indice + 1, valor)



#Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))  # 2 a's na tupla!

#contando letras nas strings
nome = tuple('Julio Cesar da Silva Jubilado')
print(nome) # ('J', 'u', 'l', 'i', 'o', ' ', 'C', 'e', 's', 'a', 'r', ' ', 'd', 'a', ' ', 'S', 'i', 'l', 'v', 'a',
# ' ', 'J', 'u', 'b', 'i', 'l', 'a', 'd', 'o')
print(nome.count('l'))  # 3 l's

#DICAS:
#Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

#Exemplo 1 Meses

meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
for indice, valor in enumerate(meses):
    print(indice + 1, valor)

'''
1 Jan
2 Fev
3 Mar
4 Abr
5 Mai
6 Jun
7 Jul
8 Ago
9 Set
10 Out
11 Nov
12 Dez
'''

print(meses[5])  # O acesso a elementos de uma tupla também é semelhante a de uma lista # Jun

# iterando com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1
#Verificamos em qual indice um elemento está naa Tupla
#print(meses.index('Play'))  # gera erro pois o elemento não existe
print(meses.index('Mar'))  # 2


meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')

#slicing
#tupla [inicio:fim:passo]
print(meses[7])  # Ago
print(meses[2::2])  # ('Mar', 'Mai', 'Jul', 'Set', 'Nov')



#Exemplo 2

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro (Imutabilidade)

#Copiando uma tupla para outra  #Em listas é Shallow copy
tupla = (1, 2, 3)
print(tupla)
nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)

"""




























