"""
LISTAS

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com diferença de serem
DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE
    do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.
Já em python:
- Dinâmico: Por que nõo possuem tamanho fixo; Criamos a lista e podemos adicionar elementos.
- Qualquer tipo de dado: As listas não possui tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.
- As listas em python são representadas por colchetes: []

"""
# Podemos facilmente checar se determinado valor está contido na lista
'''
num = 7
if num in lista4:
    print(f'Encontrei o número {num}!')
else:
    print(f'Não encontrei o número {num}!')
'''

# Podemos facilmente ordenar uma lista (.sort)
'''
(lista1.sort())
print (lista1)
'''

# Podemos contar os números de ocorrências de um valor em uma lista (.count)
'''
print(lista1.count(1)) #Quantos 1 tem na lista
print(lista5.count('e')) #Quantos e tem na lista
'''

# Adicionar elementos em listas; Para adicionar elementos e/ou valores em listas usamos a função .append
# Adiciona-se um elemento por vez
# lista1.append (12, 34, 23) #ERRO!!!!
# lista1.append ([12, 34, 23]) CORRETO!!!
'''
print(lista1)
lista1.append(42)
print(lista1)
lista1.append ([12, 34, 23])
print(lista1)
'''

'''
# Pesquisar listas dentro de listas
lista1.append([8, 3, 1])  # Adicionei essa lista dentro da lista1 (sublista)
if [8, 3, 1] in lista1: # Verifica se a lista inclusa está na lista1
    print('Encontrei o conjunto!')
else:
    print('Não encontrei o conjunto!')
'''

'''
lista1.extend([123,44,67]) # adiciona os elementos individualmente a lista, apenas iteraveis
print(lista1)
'''
'''
#Podemos inserir um novo elemento a lista informando a posição do indice.
# Não substitui o valor inicial, o mesmo será deslocado para a direita.
lista1.insert(2, 'novo valor')
print(lista1)
'''
'''
#juntar duas listas usando +
lista6 = lista1 + lista2
print (lista6)
'''
'''
#juntar duas listas usando extend
lista1.extend(lista2)
print(lista1)
'''
'''
#invertendo a ordem dos elementos da lista com REVERSE:
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
'''
'''
#invertendo a ordem dos elementos da lista com SLICE ::
print(lista1[::-1])
print(lista2[::-1])
'''
'''
#Copiar uma lista
lista6 = lista2.copy()
print(lista6)
'''
'''
#Contagem de elementos da lista usando LEN
print(len(lista1))
'''
'''
#Removendo o último elemento da lista usando POP
# O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)
'''

'''
#Podemos remover um elemento usando o indice com o POP
# Os elementos a direita foram deslocados para a esquerda
#Se não houver elemento no indice informado teremos o erro index error
lista5.pop(2)
print(lista5)
'''

'''
#Podemos ZERAR a lista
print(lista5)
lista5.clear()
print(lista5)


#Repetir os elementos da lista
print(lista5)
lista5 = lista5 * 3
print(lista5)



#CONVERTENDO um STRING para LISTA usando SPLIT
#EX 1
curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas
#Exemplo 2 (USANDO A VIRGULA COMO SEPARADOR)

curso = 'Programação,em,python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)




#CONVERTENDO LISTA EM STRING

#Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
print(lista6)
curso = ' '.join(lista6)
print(curso)

#Pega a lista 6, coloca cifrão entre cada elemento e transforma em uma string

curso = '$'.join(curso6)
print(curso)



#Podemos colocar vários dados misturados em uma lista
print(lista7)
print(type(lista6))




#ITERANDO SOBRE LISTAS COM FOR
#EX 1
for elemento in lista1:
    print(elemento)


#EX 2
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print (soma)


#EX 3
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print (soma)


#ITERANDO LISTAS COM WHILE
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)






#Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


#Acesso ao elementos de forma indexada
#           0         1        2       3
cores = ['verde', 'amarelo','azul','branco']

print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

#Acesso aos elementos de forma indexada inversa
#Para entender melhor o índice negativo pense na lista como uma roda onde
# o final de um elemento está ligado ao inicio da lista
print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde
#print(cores[-5]) #erro pois n existe indice -5


#LOOP EM FOR
for cor in cores:
    print(cor)

#LOOP EM WHILE
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


#GERAR INDICE EM UM FOR
for indice, cor in enumerate(cores):
    print(indice, cor)

#LISTAS ACEITAM REPETIÇÃO
lista = [5, 5, 5]
print(lista)

#ENCONTRAR O ÍNDICE DE UM ELEMENTO NA LISTA (INDEX)
numeros = [45, 54, 5, 67, 76, 89, 5, 98]

# Em qual indice da lista está o valor 67 ?
print(numeros.index(67))

#Em qual indice da lista está o valor 89?
print(numeros.index(89))


#Em elementos repetidos apenas exibe o índice do primeiro elemento
print(numeros.index(5)) #2

#Fazendo buscas dentro de um range
print(numeros.index(5, 3)) #buscando a posição  partindo  do indice 3

#Podemos fazer busca dentro de uma range, inicio/fim
print(numeros.index(5, 1, 4))  # Buscar o indice do valor 5 entre os índices 1 a 4



#REVISANDO SLICING

#lista[inicio:fim:passo]
# range (inicio:fim:passo)

#Trabalhando com slice de lista com o parâmetro 'inicio'

nome = 'Julio Cesar da Silva Jubilado'
lista = [1, 2, 3, 4, 5, 6]

print(lista[1:])  # iniciando do indice 1 e pegando os elementos restantes a direita
print(lista[::])  # exibe todos os elementos
print(lista[-2:])  # [3, 4]
print(lista[:-2])  # [1, 2] Começa no indice 0 e vai até o 2 - 1
print(lista[:4])  # [1, 2, 3, 4] Começa em 0 e vai até o 4 - 1
print(lista[1:3])  # [2, 3] Começa em 1 e vai até o 3 - 1

####Trabalhando com slice de lista com o parâmetro 'Passo' SLICE STEP
print(lista[1::2])  # [2, 4, 6] Começa no indice 1 e vai até o final de 2 em 2
print(lista[0::2])  # [1, 3, 5] Começa no indice 0 e vai até o final de 2 em 2
print(lista[::-1])  # [6, 5, 4, 3, 2, 1] inverte os valores de 1 em 1
print(lista[::-2])  # [6, 4, 2] inverte os valores  pulando 1
#print(lista[::0])  # ERROR SLICE STEP N PODE SER ZERO
print(nome[::-1])  # inverte todos os de 1 em 1


#invertendo valores em um lista
nomes = ['Julio', 'Cesar']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)


#invertendo valores em um lista .REVERSE
nomes.reverse()
print(nomes)
nomes.reverse()
print(nomes)


#Soma*, Valor máximo*, Valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum(lista))  # Soma os valores da lista
print(max(lista))  # Mostra o valor maximo da lista
print(min(lista))  # Mostra o valor minimo da lista
print(len(lista))  # Quantidade de elementos da lista

#Converter lista em tupla
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# DESEMPACOTAMENTO de listas
# ATENÇÃO: Se tivermos mais elementos pra desempacotar do que variaveis para receber os valores, teremos VALUE ERROR
lista = [1, 2, 3, 4, 5, 6, 7, 8]
n1, n2, n3, n4, n5, n6, n7, n8 = lista
print(n4)


#Copiando uma lista para outra (Shallow Copy e Deep copy)
#Forma 1: DEEP COPY
lista = [1, 2, 3]
print(lista)

nova = lista.copy() # Copiamos os dados da lista (lista) para outra lista (nova) LISTAS INDEPENDENTES (DEEP COPY)
print(nova)
nova.append(4)
print(nova)
print(lista)



#Forma 2: Shallow Copy  LISTAS DEPENDENTES uma da outra via atribuição
# Qualquer alteração em uma vai refletir nas outras

lista = [1, 2, 3, 4, 5, 6]
print(lista)

nova = lista

print(nova)
nova.append(4)

print(lista)
print(nova)


'''

# type ([])
# Representação de uma lista

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 234566]
cores = ['verde', 'amarelo', 'azul', 'branco']






























