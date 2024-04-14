"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas lists comprehensions

"""

#1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Vamos gerar uma lista somente com os pares:

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(pares)
print(impares)

#[2, 4, 6, 8, 10]
#[1, 3, 5, 7, 9]

#Vamos refatorar:
# Qualquer n par módulo de 2 resulta em 0 que é False. not false = True
pares = [n for n in numeros if not n % 2]

# Qualquer n impar módulo de 2 resulta é 1 que é True.
impares = [n for n in numeros if n % 2]

#[2, 4, 6, 8, 10]
#[1, 3, 5, 7, 9]

#4
res = [n * 2 if n % 2 == 0 else n / 2 for n  in numeros]
print(res)
# [0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5, 20]
