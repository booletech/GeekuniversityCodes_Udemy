"""
Tipo None:
O tipo de dado None em Python representa o tipo 'sem tipo' ou 'tipo vazio' porém falar que é
um 'tipo sem tipo' é mais apropriado.

O tipo None é sempre especificado com a primeira letra maiúscula
certo: None
Errado: None

Podemos utilizar None quando queremos criar uma variavel e inicializa-la com
um tipo 'sem tipo' antes de receber-mos um valor final.
Podendo definir o tipo no momento em que for usar a variável.

OBS: O tipo None Sempre será Falso

"""

numeros = None
print(numeros)  # None
print(type(numeros))  # <class 'NoneType'>

numeros = 1.44, 1.34, 5.67

print(numeros)  # (1.44, 1.34, 5.67)
print(type(numeros))  # <class 'tuple'>

