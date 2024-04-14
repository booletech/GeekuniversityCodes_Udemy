'''
Tipo booleano
álgebra booleana - criada por George Boole
2 Constantes, Verdadeiro ou Falso
True-> Verdadeiro
False-> False

Obs: Sempre com a inicial maiuscula
Errado: true, false
Certo: True, False
Operações básicas utilizam booleana. Imagine um sistema que verifica se um usuario esta ou não ativo em um
sistema. Usuário ativo ou não
'''

ativo = False
print(ativo)

'''Operações básicas'''
# Negação (not):
'''Fazendo a negação, se o valor booleano for verdadeiro o resultado será 
falso se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.'''

print(not ativo)
logado = False

# Ou (or):
'''É uma operação binária, ou seja depende de dois valores. Ou um ou outro deve ser verdadeiro
para que o resultado seja verdadeiro
True or True
True
True or False
True
False or False
False
False or True
True
'''
print (ativo or logado)

# E (AND)
"""Também é um a operaçãos binária, ou seja, depende de dois valores. Ambos os valores 
deve ser verdadeiro
True and True -> True
True and False -> 
False and True ->
False and False ->