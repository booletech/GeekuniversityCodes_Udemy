"""
- Conjuntos em qualquer linguagem, estamos fazendo referência a teoria dos conjuntos da matemática.
- No Python, os conjuntos são chamados de SETS.
Dito isto, da mesma forma que na matematica, conjuntos nõa possuem valores duplicados, Não possuem valores ordenados
Elementos não são acessados via indice, ou seja, conjuntos não são indexados.
Conjuntos são bons para utilizar quando precisamos analisar elementos mas não nos importamos com a ordenação deles
quando não precisamos se preocupar com chaves valores e itens duplicados.
Os conjuntos, são referenciados em python com CHAVES! {}
Diferença entre Conjuntos (sets) e mapas (dicionários) em Python:
            -Um dicionário tem chave/valor;
            -Um conjuntos tem apenas valor;

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Definindo um conjunto:
#Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)  # {1, 2, 3, 4, 5, 6, 7}
print(type(s))
# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente o mesmo será ignorado sem gerar erro
# E não fará parte do conjunto

#Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5, 5, 7, 8, 2}
print(s)  # {1, 2, 3, 4, 5, 7, 8}
print(type(s))  # <class 'set'>


#Podemos verificar se determinado elemento está contido em um conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# importante lembrar que além de não termos valores duplicados não temos ordem
# Exemplo 1

# Listas aceitam valores duplicados, entao temos 10 elementos
# A ordem dos elementos da lista é a ordem em que é declarada
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f"Lista: {lista} com {len(lista)} elementos")

# Tuplas aceitam valores duplicados, entao temos 10 elementos
# A ordem dos elementos da Tupla é a ordem em que é declarada
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')


#Dicionários não aceitam chaves duplicadas, entao temos 8 elementos
# A ordem dos elementos do dicionário é a ordem em que é declarada
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')


# Conjuntos não aceitam valores duplicados, entao temos 8 elementos
# A ordem dos elementos do conjunto é definida aleatoriamente (ele decide)
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Assim como todo outro conjunto (set) python podemos colocar tipos de dados misturados em sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))
# {1, 'b', 34.22, 44}
# <class 'set'>


# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
# 1
# b
# 34.22
# 44


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# usos interessantes com sets;
# Imagine que fizemos um formulário de cadastro de visitantes em um museu, e os visitantes
# informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista python já que em uma lista podemos adicionar novos elementos e
# ter repetição.

cidades = ['Belo horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

#  Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos:
# O que você faria? Um loop na lista para verificar e retirar as repetições ???
#Podemos utilizar SET para  isso:

print(len(set(cidades)))
# 4
# Descrição do que acontece acima:
# set(cidades) -> lista sem repetição
# (len(set(cidades)) ->  contagem de valores que estão na lista sem repetição:


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Adicionando elementos em um conjunto:

s = {1, 2, 3}
s.add(4)
print(s)
# {1, 2, 3, 4}

#Caso repita a inclusão, não será gerado erro porém não irá adicionar e o comando será ignorado


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Remover elementos em um conjunto:

s = {1, 2, 3}
print(s)

#Forma 1
s.remove(3)  # Não é índice; Informamos o valor a ser removido
print(s)

#OBS: Caso o valor não seja encontrado será gerado o erro keyError. Nenhum valor é retornado

#Forma 2
s.discard(2)
print(s)

#Obs: Se o valor nao for encontrado, nenhum erro é gerado

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Copiando um conjunto para outro:
s = {1, 2, 3, 4}
print(s)

#Copiando um conjunto para outro
#Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(5)
print(novo)
print(s)

#O conjunto original se mantém e o conjunto cópia é alterado
#Quando utiliza o deepcopy nós criamos dois objetos separados e independentes



#Copiando um conjunto para outro:
s = {1, 2, 3, 4}
print(s)

#Copiando um conjunto para outro
#Forma 1 - Deep Copy - aloca novo espaço em memória e faz uma cópia
novo = s.copy()
print(novo)

novo.add(5)
print(novo)
print(s)

#O conjunto original se mantém e o conjunto cópia é alterado
#Quando utiliza o deepcopy nós criamos dois objetos separados e independentes

#Forma 2 - Shallow Copy - Copia o valor com as variaveis independentes

novo = s
novo.add(4)

print(novo)
print(s)


#Podemos remover todos os itens de um conjunto
s.clear()
print(s)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Métodos matemáticos de conjuntos
# imagine que temos dois conjuntos: Um contendo estudantes do curso de python
# e um contendo os estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Perceba que alguns alunos estudam nas duas turmas.

#PROBLEMA:
# Precisamos gerar um conjunto com nomes de estudantes únicos (Sem repetir os nomes!)


# Forma 1 - Utilizando Union - União entre dois ou mais conjuntos

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# {'Pedro', 'Helen', 'Marcos', 'Guilherme', 'Gustavo', 'Fernando', 'Ana', 'Julia', 'Patricia'}


# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)






#PROBLEMA 2:
#Gerar um conjunto de estudantes que estão em ambos os cursos:

#FORMA 1
#utilizando o intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)


#FORMA 2
# utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)






# PROBLEMA 4
# Gere um conjunto de estudantes de um curso que não estão no outro.

# Utilizando Difference

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




"""

#Soma, valor maximo, valor minimo, tamanho
#Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
