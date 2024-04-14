"""
Reversed

Não confunda com a função reverse() que estudamos nas listas!!!
A função reverse() só funciona nas listas
A função reversed funciona com qualquer iteravel


A função reversed() retorna um iteravel chamado list reversed iterator


# Exemplo:

numeros = [1, 2, 3, 4, 5]
res = reversed(numeros)
print(res)
print(type(res))
#<list_reverseiterator object at 0x000001D5E2E89D20>
#<class 'list_reverseiterator'>




"""


# Exemplo:

numeros = [1, 2, 3, 4, 5]
res = reversed(numeros)
print(res)
print(type(res))
#<list_reverseiterator object at 0x000001D5E2E89D20>
#<class 'list_reverseiterator'>


# Podemos converter o elemento retornado para uma lista, tupla ou conjunto:

#Lists
print(list(reversed(numeros)))
# [5, 4, 3, 2, 1]

#Tuple
print(tuple(reversed(numeros)))
# (5, 4, 3, 2, 1)


#Conjunto
print(set(reversed(numeros)))
#{1, 2, 3, 4, 5}
#Sets não se importam com ordem então permanece o mesmo

# Podemos iterar sobre o reversed()
for letra in reversed('JulioCesar'):
    print(letra, end='')
# raseCoiluJ

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('JulioCesar'))))
# raseCoiluJ

# Ja vimos como fazer isso mais fácil com o slice de strings:
print('Geek University'[::-1])
# ytisrevinU keeG

# Podemos utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0


# Ja vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0

