"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens (C/Java) possuem estrutura de dados chamadas de ARRAYS
        - Unidimensionais (Arrays/Vetores);
        - Multidimensionais (Matrizes)


Em python NÃO EXISTEM ARRAYS!!!
Em python temos listas!

# Exemplos:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Como fazemos para acessar os dados?

print(listas[0])
# [1, 2, 3]
print(listas[0][1])
#2
print(listas[2][1])
# 2


#Iterando com loops em uma lista aninhada
# Vamos mostrar a lista primeiro:
for lis in listas:
    print(lis)
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]

# Para mostrar cada um dos elementos (versão FOR IN:
for lis in listas:
    for n in lis:
        print (n)
#1
#2
#3
#4
#5
#6
#7
#8
#9

# Vamos utilizar list comprehensions:
[[print(valor) for valor in lis] for lis in listas]


#1
#2
#3
#4
#5
#6
#7
#8
#9


"""
# Outros exemplos
tabuleiro = [[n for n in range(1, 4)] for valor in range (1, 4)]
print(tabuleiro)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#Jogo da velha:
velha = [['X' if n % 2 == 0 else 'O' for n in range(1, 4)] for valor in range(1, 4)]
print(velha)
#[['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]

# Gerando valores iniciais:
print([['*' for i in range (1, 4)] for j in range(1, 4)])
# [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


