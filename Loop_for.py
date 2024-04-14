"""
Loop for
Loop -> Estrutura de repetição
For  -> Uma dessas estruturas

C ou Java (Exemplo de estrutura de repetição)

for(int i=0; i<limitador; i++){
    //execução do loop
}

Python

for item in iterável:
    //execução do loop


Utilizamos Loops (for ou while) para iterar sobre sequencias ou sobre valores iteráveis ( Podemos trabalhar
com cada um dos caracteres - Ex: Strings como:
/>>> nome = 'julio'
/>>> nome
'julio'
/>>> nome [0]
/>>> 'j'

Ex: Lista
        lista = [1,2,3,4,5]
    Range
        numeros = range (1,10)
"""
'''
# Exemplo de for 1

nome = 'julio'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em um listA

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
'''
'''
# Exemplo de for 3 (iterando sobre um range)
# range(valor_inicial valor_final)
#Obs: O valor final não é incluso
for numero in range(1, 100):
    print(numero)
'''

# Os resultados abaixo são os mesmos:
'''
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
'''

'''
#Imprime cada posiçao e valor
for valor in enumerate(nome):
    print(valor)

#Imprime apenas as letras
for valor in enumerate(nome):
    print(valor[1])

#Imprime apenas as posições:
for valor in enumerate(nome):
    print(valor[0])
'''

# Obedecendo o usuário a quantidade de vezes
"""
qtd = int(input('Quantas vezes esse loop deve rodar?\n'))
for n in range(1,qtd):
    print(f'imprimindo {n}')
"""

# Realizar soma a cada vez que rodar o loop:
'''
qtd = int(input('Quantas vezes esse loop deve rodar?\n'))
soma = 0

for n in range(1,qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:\n'))
    soma = soma + num
print(f'a soma é {soma}')
'''

# Imprime os caracteres sem pular linha:
'''
nome = 'Julio'
for letra in nome:
    print(letra, end='')
'''

#Tabela de Emojis Unicode
#Para imprimir os emojis precisamos do caracter unicode:
#Exemplo: U+1F60D (original)
#Modificado: U0001F60D

# imprimindo Emojis:
'''
for num in range(1, 11):
    print('\U0001F60D' * num)
'''
#Executando 3 vezes:
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)









