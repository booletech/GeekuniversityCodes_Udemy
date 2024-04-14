"""
Map

# Faremos  o mapeamento de função e valor, bibliotecas mapeam chave:valor e são diferentes do que vamos estudar
#em maps

#MAPEAMENTO DE VALORES PARA FUNÇÃO



import math


def area(r):
    #Calcula a área de um circulo com o raio r
    return math.pi * (r ** 2)


print(area(2))
# 12.566370614359172

# Vamos calcular mais valores de raios??

raios = [2, 5, 7, 3, 10, 44]

# Forma comum
areas = []  # Lista vazia
for r in raios:  # Para cada r dentro da lista raios:
    areas.append((area(r)))  # Calcula a area de cada r dentro de raios e adiciona em areas

# Forma 2 - map

# Uma função que recebe dois parametros o primeiro: uma função; o segundo: um iterável
# retorna um MAP OBJECT
areas = map(area, raios)
print(list(areas))  # Podemos converter pra forma que quisermos nesse caso optei list mas poderia ser tupla, etc
# [12.566370614359172, 78.53981633974483, 153.93804002589985, 28.274333882308138, 314.1592653589793, 6082.12337734984]


#  Vamos converter utilizando expressão lambda
# Forma 3 - map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# [12.566370614359172, 78.53981633974483, 153.93804002589985, 28.274333882308138, 314.1592653589793, 6082.12337734984]

# APÓS A CONVERSÃO E UTILIZAÇÃO DE MAP() DEPOIS DA UTILIZAÇÃO DO RESULTADO ELE ZERA!!!!

"""

# Para fixar - MAP
# Temos dados iteráveis:
# dados: a1, a2, a3, a4, ... an
# Temos uma função:
# funcao: f(x)
# UTILIZAMOS A FUNÇÃO MAP(F, DADOS) ONDE MAP IRÁ MAPEAR CADA ELEMENTO DOS DADOS E APLICAR A FUNÇÃO
# O map object: f(a1), f(a2), f(...), f (an)


# Vamos imaginar que temos uma lista de cidades e de suas temperaturas respectivamente:
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Iorque', 28),
           ('Londres', 22)]
print(cidades)

# Foi solicitado que as temperaturas sejam exibidas em Feireheit:
# f = 9 / 5 * c + 32

#lambda
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
print (list(map(c_para_f, cidades))) # map(funcao, iteravel)
#MAP RECEBE APENAS UM PARÂMETRO!



# [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Iorque', 28),
# ('Londres', 22)]

# [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6),
# ('Nova Iorque', 82.4), ('Londres', 71.6)]

