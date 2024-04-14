"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
Exemplos:




lista = [1, 8, 4, 99, 29, 47, 43, 67, 34]
print(max(lista))
# 99
print(min(lista))
# 1

tupla = (1, 8, 4, 99, 29, 47, 43, 67, 34)
print(max(tupla))
# 99
print(min(tupla))
# 1

set = {1, 8, 4, 99, 29, 47, 43, 67, 34}
print(max(set))
# 99
print(min(set))
# 1


dicionario = dict(a=1, b=8, c=4, d=99, e=29, f=47, g=43, h=67, i=34)
print(max(dicionario, key=dicionario.get))
# d
print(min(dicionario, key=dicionario.get))
# a




# Faça m programa que receba dois valores do usuário e mostre o maior:
val1 = int(input('Informe um valor:'))
val2 = int(input('Informe outro valor:'))

print(max(val1, val2))



print(max('a', 'abc', 'ab'))  # abc
print(max('a', 'b', 'c'))  # c
print(max(3.89, 5.78))  # 5.78
print(max('Julio Cesar da Silva Jubilado'))  # v



_____________________________________________________
MIN - > Retorna o menor item de um iteravel



lista = [1, 8, 4, 99, 29, 47, 43, 67, 34]
print(max(lista))
# 99
print(min(lista))
# 1

tupla = (1, 8, 4, 99, 29, 47, 43, 67, 34)
print(max(tupla))
# 99
print(min(tupla))
# 1

set = {1, 8, 4, 99, 29, 47, 43, 67, 34}
print(max(set))
# 99
print(min(set))
# 1


dicionario = dict(a=1, b=8, c=4, d=99, e=29, f=47, g=43, h=67, i=34)
print(max(dicionario, key=dicionario.get))
# d
print(min(dicionario, key=dicionario.get))
# a




# Faça m programa que receba dois valores do usuário e mostre o maior:
val1 = int(input('Informe um valor:'))
val2 = int(input('Informe outro valor:'))

print(max(val1, val2))



print(max('a', 'abc', 'ab'))  # abc
print(max('a', 'b', 'c'))  # c
print(max(3.89, 5.78))  # 5.78
print(max('Julio Cesar da Silva Jubilado'))  # v




MIN



# Faça m programa que receba dois valores do usuário e mostre o maior:
val1 = int(input('Informe um valor:'))
val2 = int(input('Informe outro valor:'))

print(min(val1, val2))



print(min('a', 'abc', 'ab'))  # abc
print(min('a', 'b', 'c'))  # c
print(min(3.89, 5.78))  # 5.78
print(min('Julio Cesar da Silva Jubilado'))  # "espaço vazio"




nomes = ['Julio', 'Dayana', 'Marcelo', 'Jon', 'Esther']
print(max(nomes))  # Marcelo
print(min(nomes))  # Dayana
# Considera a ordem alfabética

print(max(nomes, key=lambda nome: len(nome)))  # Marcelo
print(min(nomes, key=lambda nome: len(nome)))  # Jon

"""
musicas = [
    {"Título:": "Black", "tocou": 3},
    {"Título:": "Jeremy", "tocou": 2},
    {"Título:": "Even flow", "tocou": 4},
    {"Título:": "The man", "tocou": 32},
    {"Título:": "Iron Man", "tocou": 50}

















