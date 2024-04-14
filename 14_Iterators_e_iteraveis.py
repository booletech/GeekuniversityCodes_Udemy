"""
Entendendo um iteravel e um iterable

Iterator
- Objeto de programação que pode ser iterado
- Retorna um dados sendo um elemento por vez quando uma função next() é chamada
Exemplos:
nome = 'Geek' -> String iteravel
numeros = [1, 2, 3, 4, 5, 6] lista iteravel



Iterable
    - Um objeto que irá retornar um iterator quando a função iter() for chamada



# Vamos entender melhor executando

nome = 'Julio Cesar'
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # J
print(next(it1))  # u
print(next(it1))  # l
print(next(it1))  # i
print(next(it1))  # 0

print(next(it2))  # 1
print(next(it2))  # 2
print(next(it2))  # 3
print(next(it2))  # 4
print(next(it2))  # 5
print(next(it2))  # 6



"""


nome = 'Geek'
for letra in nome:
    print(f'{letra}')
# G
# e
# e
# k

# o next controla automaticamente até onde pode contar, sem ultrapassar o limite e gerar erro