"""
len, abs, sum e Round

# Len -> Retorna o tamanho ( A quantidade de elementos em um iterável)


# Revisão

print(len('Julio'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1,'b': 2, 'c': 3,'d': 4,'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, ao executarmos a função len() o Python faz o seguinte:

#Dunder len
print('Geek University'. __len__())


____________________________________________________________________

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou Real. Retorna o valor real sem o sinal!
# FUNCIONA APENAS COM NÚMEROS !

# Exemplo abs

print(abs(-45))  # 45
print(abs(-456))  # 456
print(abs(90))  # 90
print(abs(-98.5))  # 98.5

_______________________________________________________


# Sum
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a
soma total dos elementos incluindo o valor inicial.
# O valor inicial default = 0

EX:


print(sum([1, 2, 3, 4, 5]))
# 15
print(sum([1, 2, 3, 4, 5], -5))
# 10
print(sum([1, 2, 3, 4, 5], 5))
# 20

# Flutuantes
print(sum([3.57, 2.78, 34.9]))  # 41.25

# set
print(sum({3.57, 2.78, 34.9}))  # 41.25

#tupla
print(sum((3.57, 2.78, 34.9)))  # 41.25

# Dict
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))  # 6

____________________________________________________________________


ROUND

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão
não for informado retorna o inteiro mais próximo da entrada.

# Exemplos Round

print(round(3.45, 1))  # 3.5
print(round(45.77777))  # 46
print(round(45.787878, 2))  # 45.79
print(round(45.543543543, 3))  # 45.544





"""













