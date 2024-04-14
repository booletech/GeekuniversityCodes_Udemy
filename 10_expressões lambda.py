"""
Expressão lambdas
conhecidas por expressões lambdas ou simplesmente lambdas
são funções sem nome (anônimas)

#UTILIZADAS EM FILTRAGEM E ORDENAÇÃO DE DADOS

Vamos lembrar um função em python:

def soma (a, b):
    return a + b

#2

def funcao(x):
    return 3 * x + 1


print(funcao(4))
#13


def funcao(x):
    return 3 * x + 1


print(funcao(4))
# 13

# Esse mesmo exemplo utilizando expressão lambda
lambda x: 3 * x + 1  # FAZ EXATAMENTE O QUE FIZEMOS ACIMA!!!

# Como utilizar??
calc = lambda x: 3 * x + 1
print(calc(4))
# 13
# Essa forma não é a ideal para utilizar expressões lambda

__________________________________________________
# Podemos ter expressões lambdas com múltiplas entradas:

# EX1

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('julio', 'cesar'))
print(nome_completo('DAYANA', 'MARtins'))
print(nome_completo('julio', 'jUbilado'))
#Julio Cesar
#Dayana Martins
#Julio Jubilado

# estrutura:
# nomedafuncao = lambda entrada, entrada, entrada: retorno da funcao

# EM FUNÇÕES PYTHON PODEMOS TER NENHUMA OU VÁRIAS ENTRADAS, EM LABDAS TAMBÉM!
# Exemplo:

nome = lambda: 'relatorio'
potencia = lambda u, i: u * i
duas = lambda x, y: (x * y) + 2
tres = lambda x, y, z: 3 / (x + y + z)

# Estrutura:
# n = lambda x1, x2, x3 ... xn: <expressão>

print(nome())  # relatorio
print(potencia(110, 3500))  # 385000
print(duas(3, 4))  # 14
print(tres(3, 4, 5))  # 0.25

# Se passarmos mais parâmetros ou mais argumentos do que parâmetros esperados teremos TYPE ERROR!!!!

# Outro exemplo:

_________________________________________________________________________________________________

autores = [
    'J.K. Rowling',
    'George Orwell',
    'Jane Austen',
    'Stephen King',
    'Agatha Christie',
    'Gabriel García Márquez',
    'Haruki Murakami',
    'J.R.R. Tolkien',
    'Dan Brown',
    'Aldous Huxley',
    'Emily Brontë',
    'F. Scott Fitzgerald',
    'Leo Tolstoy',
    'Margaret Atwood',
    'Isaac Asimov',
    'Ernest Hemingway',
    'Toni Morrison',
    'Mark Twain',
    'Roald Dahl',
    'Herman Melville'
]

print(autores)

#Vamos ordenar essa lista pelo sobrenome?
# Primeiro vamos criar uma expressão lambda que extrai os sobrenomes:


# nome.split(' ')[-1].lower
# nome.split(' ') -> Será gerada uma lista com as palavras do nome
# nome.split(' ')[-1] -> Será selecionado o último elemento da lista
# nome.split(' ')[-1].lower -> Tranforma tudo em minúsculo

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# ['Isaac Asimov', 'Margaret Atwood', 'Jane Austen', 'Emily Brontë', 'Dan Brown', 'Agatha Christie', 'Roald Dahl',
# 'F. Scott Fitzgerald', 'Ernest Hemingway', 'Aldous Huxley', 'Stephen King', 'Herman Melville', 'Toni Morrison',
# 'Haruki Murakami', 'Gabriel García Márquez', 'George Orwell', 'J.K. Rowling', 'J.R.R. Tolkien', 'Leo Tolstoy',
# 'Mark Twain']

# A função .sort coloca em ordem alfabetica!

_____________________________________________________________________________________________________



"""


# Em games de tiro podemos precisar utilizar funções quadraticas para calcular trajetória de projéteis
# Vamos utilizar um exemplo:

# Função Quadrática
# f(x): a * x **2 + b * x + c

# Definindo a funcao

def ger_fun_quad(a, b, c): #Uma função que recebe três valores a, b, c
    """Retorna a função f(x): a * x **2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c
    # O lambda será o retorno da função
    # O lambda recebe um parâmetro x e retorna a função quadratica


teste = ger_fun_quad(2, 3, -5) # a, b, c

# Abaixo temos os valores de x print(teste(x))
print(teste(0))  # -5
print(teste(1))  # 0
print(teste(2))  # 9

# Outra forma, sem renomear a função:
print(ger_fun_quad(3, 0, 1)(2)) # 3, 0, 1 -> a, b, c ; 2 -> x
# 13

