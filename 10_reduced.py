"""
Reduce
Obs: A partir do Python 3+ a função reduce() não é mais uma função integrada (Built in)
Agora temos que importar do módulo 'functools'

Guido van Rossum: Utilize a função reduce se você REALMENTE precisa dela.
Utilize a função reduce () se você REALMENTE precisa dela. Na maioria das vezes
um loop for é mais legível!

#Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, ..., an ]
# Você tem uma função que recebe 2 PARÂMETROS:
def funcao (x, y):
    return x * y
# Assim como map() e filter() a função reduce() recebe dois parâmetros: função e iterável
reduce(funcao, dados)
# A função reduce funciona da seguinte forma:
        Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
        Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e
        Guarda o resultado e assi por diante

    Ou seja, em cada passo dado ela aplica a função passando como primeiro argumento o resultado anterior. No final
    reduce() irá retornar o resultado final

Alternativamente poderiamos enxergar a função reduce() como:
funcao(funcao(funcao(a1, a2),a3),a4),...),an)



"""

# Exemplo prático!

# Vamos multiplicar todos os números de uma lista utilizando a função reduce()

from functools import reduce
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
# Para Utilizar o reduce() precisamos de uma função que recebe DOIS parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)
#25878772920
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
# E assim por diante até finalizar os números

#Vamos utilizar um loop normal para fazer o mesmo:
res = 1
for n in dados:
    res = res * n
print(res)
# 25878772920

# A PRINCIPAL DIFERENÇA ENTRE O REDUCE() E OS OUTROS É QUE É NECESSARIO DOIS VALORES!!!



