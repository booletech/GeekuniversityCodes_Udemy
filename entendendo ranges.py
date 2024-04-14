"""
Precisamos conhecer o loop for para usar o range;
Para trabalhar melhor com loops for precisamos usar o range.

Ranges são utilizados para gerar sequencias numéricas não
de forma aleatória mas sim de maneira especificada

formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrao 0, e passo de 1 em 1)
"""

# Forma 1
'''
for num in range(11):
    print(num)
'''

# Forma 2
# range(valor_de_inicio, valor_de_parada)
# OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)
'''
for num in range(4,11):
    print(num)
'''

# Forma 3
# range(valor_de_inicio, valor_de_parada, passo)
'''
for num in range (1, 10, 2):
    print(num)
'''

# Forma 4(inversa)
# range(valor_inicio, valor_de_parada, passo)
for num in range(10, -1, -1):
    print(num)

