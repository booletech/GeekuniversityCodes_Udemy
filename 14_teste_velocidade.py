"""
Teste de velocidade com expressões geradoras

# Vamos entender as diferenças entre generators e expressões geradoras



def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator #  <generator object nums at 0x000001E0AF279A10>
print(next(ge1))  # 1
print(next(ge1))  # 2
print(next(ge1))  # 3
print(next(ge1))  # 4
print(next(ge1))  # 5


# GENERATOR EXPRESSION

ge2 = (num for num in range(1,  10))
print(ge2)  # <generator object <genexpr> at 0x0000025EB7B861F0>
print(next(ge2))  # 1
print(next(ge2))  # 2
print(next(ge2))  # 3
print(next(ge2))  # 4
print(next(ge2))  # 5



"""

# Conseguimos utilizar várias funções integradas do python
# Se quisermos somar todos os valores podemos fazer o seguinte:

# REALIZANDO O TESTE DE VELOCIDADE
import time

gen_inicio = time.time()  # Qual é o tempo inicial?
print(sum(num for num in range(100000000)))  # Gera a expressão gerando ela e no final somando
gen_tempo = time.time() - gen_inicio # Tempo total

list_inicio = time.time()
print(sum([num for num in range(100000000 )]))
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}')
print(f' List Comprehension levou {list_tempo}')

# 4999999950000000
# 4999999950000000
# Generator expression levou 11.750003099441528
# List Comprehension levou 34.3995885848999


